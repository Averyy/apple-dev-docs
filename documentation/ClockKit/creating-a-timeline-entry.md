# Creating a timeline entry

**Framework**: Clockkit

Package your app-specific data into a template and create a timeline entry for that template.

#### Overview

ClockKit periodically requests timeline entries from your complication’s data source. A timeline entry consists of a complication template that you have configured with your app’s data and a date that specifies when ClockKit displays that template.

![A figure showing the app data, timeline entry date, and template for a timeline entry.](https://docs-assets.developer.apple.com/published/521293196c639304b3ff24a6b9a837a0/media-3165033%402x.png)

Your data source packages app-specific data into a template that ClockKit can display onscreen. To create the template, you examine the provided [`CLKComplication`](clkcomplication.md) object, select an appropriate template, fill the template with data from your app, and then create a timeline entry for the template.

##### Examine the Complication Object

When ClockKit requests a template, it always provides a [`CLKComplication`](clkcomplication.md) object that describes the complication. The complication has an [`identifier`](clkcomplication/identifier.md) that your app defines, and a [`family`](clkcomplication/family.md) from the [`CLKComplicationFamily`](clkcomplicationfamily.md) enumeration. Each [`identifier`](clkcomplication/identifier.md) defines a separate complication type for the specified [`family`](clkcomplication/family.md).

Examine the [`identifier`](clkcomplication/identifier.md) to determine which kind of complication you’re creating. In watchOS 7 and later, your app can provide one or more complications per [`family`](clkcomplication/family.md). For example, a weather app may support separate complications for the `Condition`, `Temperature`, and `Precipitation` identifiers.

```swift
switch complication.identifier {
case complicationConditionIdentifier:
    templateOrNil = myGetConditionTemplate(for: family, date: date)
    
case complicationTemperatureIdentifier:
    templateOrNil = myGetTemperatureTemplate(for: family, date: date)
    
case complicationPrecipitationIdentifier:
    templateOrNil = myGetPrecipitationPercentageTemplate(for: family, date: date)
```

The ClockKit framework organizes complications into families. Each family defines the size and shape of the complication. Examine the [`family`](clkcomplication/family.md) to discover which kind of template you can use. For the complete list of families, see [`CLKComplicationFamily`](clkcomplicationfamily.md).

```swift
switch complication.family {
case .circularSmall:
    // Create a template from the circular small family.
    
case .modularSmall:
    // Create a template from the modular small family.
    
case .modularLarge:
    // Create a template from the modular large family.
    
// Continue with all the templates supported by the specified type.
    
@unknown default:
    print("*** Unknown Complication Family: \(complication.family) ***")
    // Handle the error here.
}
```

Each family provides one or more templates that define the type of data and the data’s position within the complication.

Select and create a template for the specified family from the following pages:

- [`Circular small`](circular-small.md)
- [`Extra large`](extra-large.md)
- [`Modular small`](modular-small.md)
- [`Modular large`](modular-large.md)
- [`Utilitarian`](utilitarian.md)
- [`Graphic`](graphic.md)

> **Note**:  For watchOS 6 and earlier, your app can provide only one complication per family. To support these versions of watchOS, you only need to check the complication’s [`family`](clkcomplication/family.md) property when determining which template to use.

##### Create Data Providers to Fill the Template

Data providers take a raw value and format it for the template. For example, the [`CLKSimpleTextProvider`](clksimpletextprovider.md) takes two strings—a short string and a long string. If you provide both, ClockKit selects the best string for the template’s size.

```swift
let temperature = myCity.temperature(date)

let nameProvider = CLKSimpleTextProvider(
    text: myCity.name,
    shortText: myCity.abbreviation)

let temperatureProvider = CLKSimpleTextProvider(
    text: "\(longNumberFormatter.string(from: NSNumber(value: temperature)) ?? "Unknown")º F",
    shortText: shortNumberFormatter.string(from: NSNumber(value: temperature)) ?? "??")
```

ClockKit uses data providers for text, images, and gauges, including:

- [`CLKSimpleTextProvider`](clksimpletextprovider.md)
- [`CLKDateTextProvider`](clkdatetextprovider.md)
- [`CLKTimeTextProvider`](clktimetextprovider.md)
- [`CLKRelativeDateTextProvider`](clkrelativedatetextprovider.md)
- [`CLKTimeIntervalTextProvider`](clktimeintervaltextprovider.md)
- [`CLKImageProvider`](clkimageprovider.md)
- [`CLKFullColorImageProvider`](clkfullcolorimageprovider.md)
- [`CLKSimpleGaugeProvider`](clksimplegaugeprovider.md)
- [`CLKTimeIntervalGaugeProvider`](clktimeintervalgaugeprovider.md)

Some of the data providers, like [`CLKRelativeDateTextProvider`](clkrelativedatetextprovider.md) and [`CLKTimeIntervalGaugeProvider`](clktimeintervalgaugeprovider.md), automatically update the complication as time passes without affecting your complication’s background execution budgets.

Use the data providers to create and populate your template.

```swift
let template = CLKComplicationTemplateModularSmallStackText(
    line1TextProvider: temperatureProvider,
    line2TextProvider: nameProvider)
```

##### Use Complication Data

The [`CLKComplicationDescriptor`](clkcomplicationdescriptor.md) class’s `userInfo` and `userActivity` properties let you pass additional data about the complication. You can use this data to simplify creating timeline entires, and to launch a particular scene in your app.

For example, you can create a set of complications from the user’s favorite city list, as shown in [`Dynamically Define Descriptors`](declaring-complications-for-your-app#Dynamically-Define-Descriptors.md). Instead of parsing the complications identifier, you can add the city and the weather data type to the complication’s [`userInfo`](clkcomplication/userinfo.md) dictionary. Then, to create a timeline entry, you read the data from the dictionary before selecting and filling your template.

```swift
let city: City

// Read the city id from the complication's userInfo dictionary.
if let cityID = complication.userInfo?[myCityIDKey] as? String {
    city = myData.lookupCity(byID: cityID) ?? myData.currentCity
} else {
    city = myData.currentCity
}

let nameProvider = CLKSimpleTextProvider(
    text: city.name,
    shortText: city.abbreviation)

// Read the complication type from the userInfo dictionary.
let typeIdentifier = complication.userInfo?[myTypeIdentifierKey] as? String ?? "Undefined"
```

##### Create the Timeline Entry Object

Create a [`CLKComplicationTimelineEntry`](clkcomplicationtimelineentry.md) object using the template and the desired date. For the current timeline entry, you must specify a date equal to or earlier than the current time.

```swift
CLKComplicationTimelineEntry(date: Date(), complicationTemplate: template)
```

For future timeline entries, specify the date and time for the data to appear on the complication. For a meeting complication, you might display information about a meeting before its scheduled start time. For more information on creating future timeline entries, see [`Loading future timeline events`](loading-future-timeline-events.md).

## See Also

- [Enabling Complications for Your watchOS App](enabling-complications-for-your-watchos-app.md)
  Set up your watchOS app’s complications.
- [Adding Placeholders for Your Complication](adding-placeholders-for-your-complication.md)
  Provide the placeholders that users see when adding your complication to a watch face.
- [Creating complications for your watchOS app](creating-complications-for-your-watchos-app.md)
  Set up and implement complications for your watchOS app.
- [Declaring complications for your app](declaring-complications-for-your-app.md)
  Define the complications that your app supports.
- [Loading future timeline events](loading-future-timeline-events.md)
  Preserve battery life and improve performance on the watch by providing a timeline with expected data and updates.
- [Keeping your complications up to date](keeping-your-complications-up-to-date.md)
  Replace or extend the data in your complication’s timeline.
- [Building complications with SwiftUI](building-complications-with-swiftui.md)
  Design the appearance of a graphic complication using SwiftUI.
- [Displaying progress views and gauges](displaying-progress-views-and-gauges.md)
  Add rich visual data to your SwiftUI complications with progress views and gauges.
- [Adding text to a complication](adding-text-to-a-complication.md)
  Use text in SwiftUI complications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ClockKit/creating-a-timeline-entry)*