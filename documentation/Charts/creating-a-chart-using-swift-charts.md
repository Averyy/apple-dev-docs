# Creating a chart using Swift Charts

**Framework**: Swift Charts

Make a chart by combining chart building blocks in SwiftUI.

#### Overview

Help people understand complex data by focusing on what you want to communicate and who you’re communicating to. For example, suppose that you have a collection of colorful toy shapes:

![A collection of cubes, spheres, and pyramids that appear in pink, yellow, purple, and green, all lying on a plane.](https://docs-assets.developer.apple.com/published/e8ebe6ee2e8c5c0f78807b983a145fc2/CreatingYourFirstChart-1%402x.png)

You can formulate questions about this data that you’d like to answer, like which toy shape appears the most, or how many toys are green? One way to represent your data is to collect it into a table. A table organizes the data into columns and rows so it can be easily inspected. For example, you can record how many shapes of each color you have:

|  | Cube | Sphere | Pyramid | Total |
| --- | --- | --- | --- | --- |
|  | 1 | 2 | 0 | 3 |
|  | 1 | 1 | 2 | 4 |
|  | 1 | 1 | 1 | 3 |
|  | 2 | 0 | 1 | 3 |
|  | 5 | 4 | 4 | 13 |

However, in many cases, a more effective data representation is a chart. A chart allows you to communicate large amounts of information all at once. The kind of chart that you create and the way you configure the chart depend on what you want to show. To create a chart with Swift Charts, define your data and initialize a [`Chart`](chart.md) view with marks and data properties. Then use modifiers to customize different components of the chart, like the legend, axes, and scale.

##### Define the Data Source

Think about a chart as an answer to your questions. Suppose you want to know which toy shape appears the most. Start by visualizing how many of each shape you have. To display this information with a chart, create a `ToyShape` structure that represents the information that you want to visualize:

```swift
struct ToyShape: Identifiable {
    var type: String
    var count: Double
    var id = UUID()
}
```

Then, initialize an array of `ToyShape` structures to hold the data from the table:

```swift
var data: [ToyShape] = [
    .init(type: "Cube", count: 5),
    .init(type: "Sphere", count: 4),
    .init(type: "Pyramid", count: 4)
]
```

In a real app, you might download this data from a network connection, or load it from a file.

##### Initialize a Chart View and Create Marks

Create a [`Chart`](chart.md) view that serves as a container for the data series that you want to draw:

```swift
import SwiftUI
import Charts

struct BarChart: View {
    var body: some View {
        Chart {
            // Add marks here.
        }
    }
}
```

Inside the chart, specify the graphical marks that represent the data. You can populate it with a variety of kinds of marks, like [`BarMark`](barmark.md), [`PointMark`](pointmark.md) or [`LineMark`](linemark.md), that plot your data. The kind of mark that you choose depends on how you want to visualize the data. For example, you can use [`LineMark`](linemark.md) to create a line chart or [`PointMark`](pointmark.md) to produce a scatter plot. In this case, creating a bar chart is a good way to convey the number of each type of toy shape, so you use [`BarMark`](barmark.md):

```swift
Chart {
    BarMark(
        x: .value("Shape Type", data[0].type),
        y: .value("Total Count", data[0].count)
    )
    BarMark(
         x: .value("Shape Type", data[1].type),
         y: .value("Total Count", data[1].count)
    )
    BarMark(
         x: .value("Shape Type", data[2].type),
         y: .value("Total Count", data[2].count)
    )
}
```

The resulting chart clearly communicates that the cube toy shape appears the most:

![A bar chart with three bars. The first bar has a height of five and has the label Cube below the bar. The second bar has a height of four and has the label Sphere below the bar. The third bar has a height of 4 and has the label Pyramid below the bar. The first bar has a call out that identifies it as a type of Mark, specifically a BarMark. The bar chart also has labels on the x-axis and the y-axis. The number scale appears on the right side of the chart where the number 4 has a call out that marks it as an Axis Label. The scale has a minimum of zero and a maximum of six.](https://docs-assets.developer.apple.com/published/10bd600c6f8df9ac57bd337b0d2d05fb/CreatingYourFirstChart-2%402x.png)

Scale determines the position, height, and color of each `BarMark`. As you plot data on the y-dimension, the framework automatically generates axis labels for the y-axis to map the data values. The scale for the y-dimension is adjusted to match the range of totals for the shape’s group.

The above code lists each [`BarMark`](barmark.md) individually. However, for regular, repetitive data, you can use a [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach) structure to represent the same chart more concisely:

```swift
Chart {
    ForEach(data) { shape in
        BarMark(
            x: .value("Shape Type", shape.type),
            y: .value("Total Count", shape.count)
        )
    }
}
```

##### Explore Additional Data Properties

The above bar chart shows how much of each type of toy shape there are, but the earlier table separates each toy shape by color as well. A stacked bar chart can visualize not only the amount of each toy shape type, but also the distribution of colors among the shapes. Before you can plot this new information, you need to represent color in your data structure:

```swift
struct ToyShape: Identifiable {
    var color: String
    var type: String
    var count: Double
    var id = UUID()
}
```

Then update the initialized data to include the color information:

```swift
var stackedBarData: [ToyShape] = [
    .init(color: "Green", type: "Cube", count: 2),
    .init(color: "Green", type: "Sphere", count: 0),
    .init(color: "Green", type: "Pyramid", count: 1),
    .init(color: "Purple", type: "Cube", count: 1),
    .init(color: "Purple", type: "Sphere", count: 1),
    .init(color: "Purple", type: "Pyramid", count: 1),
    .init(color: "Pink", type: "Cube", count: 1),
    .init(color: "Pink", type: "Sphere", count: 2),
    .init(color: "Pink", type: "Pyramid", count: 0),
    .init(color: "Yellow", type: "Cube", count: 1),
    .init(color: "Yellow", type: "Sphere", count: 1),
    .init(color: "Yellow", type: "Pyramid", count: 2)
]
```

To represent this additional dimension of information, add the [`foregroundStyle(by:)`](chartcontent/foregroundstyle(by:).md) method to the [`BarMark`](barmark.md), and indicate the data’s color property as the plottable value:

```swift
Chart {
    ForEach(stackedBarData) { shape in
        BarMark(
            x: .value("Shape Type", shape.type),
            y: .value("Total Count", shape.count)
        )
        .foregroundStyle(by: .value("Shape Color", shape.color))
    }
}
```

The chart now splits the bars into different parts that represent the number of colors for each shape:

![A stacked bar chart showing the count of shape types with a legend. The first bar is labeled Cube, and is split into four segments of different colors. The other two are labeled Pyramid and Sphere, and each is split into three segments of different colors. A legend at the bottom of the chart indicates what each segment color represents, which is a shape color. The colors used by the chart to create the marks don’t match the shape colors that they represent. For example, the color that represents green shapes is pink.](https://docs-assets.developer.apple.com/published/aa183eca90a2e1b597d1f03a03aeee6e/CreatingYourFirstChart-3%402x.png)

The stacked bar chart chooses colors to represent the new data, and adds a legend to indicate which color represents which kind of data.

##### Customize Your Chart

For many charts, the default configuration works well. However, in this case, the colors that the framework assigns to each mark don’t match the shape colors that they represent. You can customize the chart to override the default color scale by adding the [`chartForegroundStyleScale(_:)`](https://developer.apple.com/documentation/SwiftUI/View/chartForegroundStyleScale(_:)) chart modifier:

```swift
Chart {
    ForEach(stackedBarData) { shape in
        BarMark(
            x: .value("Shape Type", shape.type),
            y: .value("Total Count", shape.count)
        )
        .foregroundStyle(by: .value("Shape Color", shape.color))
    }  
}
.chartForegroundStyleScale([
    "Green": .green, "Purple": .purple, "Pink": .pink, "Yellow": .yellow
])
```

Now the names of the colors match the colors used in the chart, making the chart easier to understand:

![A stacked bar chart showing the count of shape types with a legend. The first bar is labeled Cube, and is split into four segments of different colors. The other two are labeled Pyramid and Sphere, and each is split into three segments of different colors. A legend at the bottom of the chart indicates what each segment color represents, which is a shape color. The legend shows that the color of bar marks match the shape colors that they represent. For example, the color green is labeled Green, indicating that green marks in the chart represent green shapes.](https://docs-assets.developer.apple.com/published/a2edaec71be31fe5fa54116d6ea12a5c/CreatingYourFirstChart-4%402x.png)

This chart makes the relationship between shape counts and colors clear. You can customize charts in many other ways. For example, you can set the bar width, choose different legend symbols, and control the axes.

## See Also

- [Visualizing your app’s data](visualizing-your-app-s-data.md)
  Build complex and interactive charts using Swift Charts.
- [struct Chart](chart.md)
  A SwiftUI view that displays a chart.
- [protocol ChartContent](chartcontent.md)
  A type that represents the content that you draw on a chart.
- [struct ChartContentBuilder](chartcontentbuilder.md)
  A result builder that you use to compose the contents of a chart.
- [struct Plot](plot.md)
  A mechanism for grouping chart contents into a single entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/creating-a-chart-using-swift-charts)*