# Representing chart data as an audio graph

**Framework**: Accessibility

Define accessible representations of your chart’s components for VoiceOver to construct an audible representation of the data.

#### Overview

To represent your chart as an accessible audio graph, adopt the [`AXChart`](axchart.md) protocol on your chart’s view model. Set the [`accessibilityChartDescriptor`](axchart/accessibilitychartdescriptor.md) property to an [`AXChartDescriptor`](axchartdescriptor.md) that contains all the semantic information you need to represent your chart through an audio interface, like the chart’s title, axes, data points, and a summary of the chart’s key takeaways.

```swift
class MyChartView: UIView, AXChart {
    var accessibilityChartDescriptor: AXChartDescriptor?
}
```

For example, a chart that plots vehicle weight against fuel efficiency by country and MSRP has four data axes:

- The x-axis corresponds to the car’s weight in tons.
- The y-axis corresponds to the car’s fuel efficiency in MPG.
- The visual size of each data point corresponds to the car’s MSRP.
- The color of each data point corresponds to the car’s country of origin.

To create an audio graph of your chart, first set up a representation of each of your data points based on the information in your data model. Use that array of data points to create a — a container that describes a collection of data points. Simple data sets might only have one series of data; more complex data sets might have multiple series.

```swift
let cars = generateData()

// Generate the data points from the model data.
let dataPoints = cars.map({
    return AXDataPoint(x: $0.weight,
                       y: $0.mpg,
        additionalValues: [.number($0.msrp), .category($0.country)],
                   label: "\($0.make) \($0.model)")
})

// Make the series descriptor.
let series = AXDataSeriesDescriptor(name: "Cars",
                            isContinuous: false,
                              dataPoints: dataPoints)
```

Next, set up descriptors for the chart’s axes. For numeric axes, use the [`valueDescriptionProvider`](axnumericdataaxisdescriptor/valuedescriptionprovider.md) closure to format the data values into string representations that include the units. Consider using a formatter, like [`NSNumberFormatter`](https://developer.apple.com/documentation/foundation/nsnumberformatter) or [`NSDateFormatter`](https://developer.apple.com/documentation/foundation/nsdateformatter), to generate strings that have more complex formats.

```swift
// Make the axis descriptors.
let weight = AXNumericDataAxisDescriptor(title: "Weight",
                                         range: 0...5,
                             gridlinePositions: [0, 1, 2, 3, 4, 5]) { value -> String in
    let format = NSLocalizedString("%.2f tons",
                           comment: "Format string for values in tons")
    return String.localizedStringWithFormat(format, value)
}

let mpg = AXNumericDataAxisDescriptor(title: "Fuel Efficiency",
                                      range: 0...50,
                          gridlinePositions: [0, 10, 20, 30, 40, 50]) { value -> String in
    let format = NSLocalizedString("%ld miles per gallon",
                           comment: "Format string for values in miles per gallon")
    return String.localizedStringWithFormat(format, value)
}

let msrp = AXNumericDataAxisDescriptor(title: "MSRP",
                                       range: 0...150000,
                           gridlinePositions: []) { value -> String in
    let format = NSLocalizedString("%ld MSRP",
                           comment: "Format string for MSRP values")
    return String.localizedStringWithFormat(format, value)
}

let country = AXCategoricalDataAxisDescriptor(title: "Country",
                                      categoryOrder: cars.compactMap{ $0.country })
```

To help provide context around the chart’s data, include a localized title and consider creating a summary that summarizes the key takeaways of the data in the chart.

```swift
// Write a localized title for the chart.
let title = NSLocalizedString("Vehicle Weight vs Fuel Efficiency by Country and MSRP",
                              comment: "Chart title for fuel efficiency vs mpg chart")

// Write a summary of the chart's data.
let summary = NSLocalizedString("The chart shows that fuel efficiency decreases as vehicle weight increases.",
                                comment: "Chart summary for fuel efficiency vs mpg chart")
```

Then, create your chart descriptor based on the individual descriptors of the chart’s components.

```swift
// Make and set the chart descriptor.
accessibilityChartDescriptor = AXChartDescriptor(title: title,
                                                 summary: summary,
                                                 xAxis: weight,
                                                 yAxis: mpg,
                                                 additionalAxes: [msrp, country],
                                                 series: [series])
```

The resulting chart descriptor produces an audio graph with weight as time, MPG as pitch, MSRP as tone length, and country of origin as timbre.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/representing-chart-data-as-an-audio-graph)*