# CLKComplicationDescriptor

**Framework**: ClockKit  
**Kind**: class

A descriptor that defines a complication and the families that it supports.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
class CLKComplicationDescriptor
```

## Mentions

- [Declaring complications for your app](declaring-complications-for-your-app.md)
- [Creating a timeline entry](creating-a-timeline-entry.md)

#### Overview

Use complication descriptors to define the different types of complications that your app supports. Each descriptor provides a unique identifier for the complication, and the list of families that the complication supports. ClockKit defines the available families using the [`CLKComplicationFamily`](clkcomplicationfamily.md) enumeration, while your app can define as many identifiers as it needs. Each unique [`identifier`](clkcomplication/identifier.md) within your app represents a separate complication in the complication picker. For example, a weather app may have separate descriptors for `Condition`, `Temperature`, and `Precipitation.`

```swift
// Create the condition descriptor.
let conditionDescriptor = CLKComplicationDescriptor(
    identifier: complicationConditionIdentifier,
    displayName: "Weather Condition",
    supportedFamilies: mySupportedFamilies)

// Create the temperature descriptor.
let temperatureDescriptor = CLKComplicationDescriptor(
    identifier: complicationTemperatureIdentifier,
    displayName: "Temperature",
    supportedFamilies: mySupportedFamilies)

// Create the precipitation descriptor.
let precipitationDescriptor = CLKComplicationDescriptor(
    identifier: complicationPrecipitationIdentifier,
    displayName: "Percipitation",
    supportedFamilies: mySupportedFamilies)
```

You can dynamically create unique identifiers to further customize the complications. For example, if the weather app provides separate complications for all the cities in the user’s favorite city list, it can create a separate descriptor for each city and weather data pair. The app can create unique identifiers by appending the city name and the weather data’s name.

```swift
func getComplicationDescriptors(handler: @escaping ([CLKComplicationDescriptor]) -> Void) {
    var descriptors = [CLKComplicationDescriptor]()
    
    for city in myData.favoriteCities {
        
        let conditionIdentifier = complicationConditionIdentifier + ": \(city.id)"
        let temperatureIdentifier = complicationTemperatureIdentifier + ": \(city.id)"
        let perceptionIdentifier = complicationPrecipitationIdentifier + ": \(city.id)"
        
        // Create the descriptors for the city.
        descriptors.append(CLKComplicationDescriptor(
                            identifier: conditionIdentifier,
                            displayName: "\(city.abbreviation) Weather Condition",
                            supportedFamilies: CLKComplicationFamily.allCases,
                            userInfo: [myCityIDKey: city.id,
                                       myTypeIdentifierKey: conditionIdentifier]))

        descriptors.append(CLKComplicationDescriptor(
                            identifier: temperatureIdentifier,
                            displayName: "\(city.abbreviation) Temperature",
                            supportedFamilies: CLKComplicationFamily.allCases,
                            userInfo: [myCityIDKey: city.id,
                                       myTypeIdentifierKey: temperatureIdentifier]))

        descriptors.append(CLKComplicationDescriptor(
                            identifier: perceptionIdentifier,
                            displayName: "\(city.abbreviation) Percipitation",
                            supportedFamilies: CLKComplicationFamily.allCases,
                            userInfo: [myCityIDKey: city.id,
                                       myTypeIdentifierKey: perceptionIdentifier]))
        
    }
    
    // The order of the descriptors array
    // determines the order in the complication picker.
    handler(descriptors)
}
```

When dynamically creating identifiers, consider using the descriptor’s [`userInfo`](clkcomplicationdescriptor/userinfo.md) property to contain any additional information your app needs to create timeline entries for the complication. In the above example, the weather app adds the `myCityIDKey` and `myTypeIdentifierKey` `keys` so that it can access the city and weather data type without parsing the `identifier` string.

## Topics

### Creating descriptors
- [convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily])](clkcomplicationdescriptor/init(identifier:displayname:supportedfamilies:).md)
  Returns a new complication descriptor.
- [convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily], userActivity: NSUserActivity)](clkcomplicationdescriptor/init(identifier:displayname:supportedfamilies:useractivity:).md)
  Returns a new complication descriptor with an associated user activity.
- [convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily], userInfo: [AnyHashable : Any])](clkcomplicationdescriptor/init(identifier:displayname:supportedfamilies:userinfo:).md)
  Returns a new complication descriptor with an associated dictionary of user data.
### Accessing the descriptor’s data
- [var identifier: String](clkcomplicationdescriptor/identifier.md)
  A string that uniquely identifies the descriptor.
- [var displayName: String](clkcomplicationdescriptor/displayname.md)
  A localized string that identifies complications from the descriptor to the user.
- [var supportedFamilies: [CLKComplicationFamily]](clkcomplicationdescriptor/supportedfamilies-4ckbx.md)
  The families that support this type of complication.
- [var userActivity: NSUserActivity?](clkcomplicationdescriptor/useractivity.md)
  A user activity object that represents the state of the app at a moment in time.
- [var userInfo: [AnyHashable : Any]?](clkcomplicationdescriptor/userinfo.md)
  A dictionary of data that your data source can use to generate timeline entries.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Migrating ClockKit complications to WidgetKit](../WidgetKit/Converting-A-ClockKit-App.md)
  Leverage WidgetKit’s API to create watchOS complications using SwiftUI.
- [protocol CLKComplicationDataSource](clkcomplicationdatasource.md)
  A protocol that provides ClockKit with information about your complication.
- [let CLKDefaultComplicationIdentifier: String](clkdefaultcomplicationidentifier.md)
  An identifier representing a default complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor)*