# CLKComplicationDescriptor

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A descriptor that defines a complication and the families that it supports.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
class CLKComplicationDescriptor
```

```objc
@interface CLKComplicationDescriptor : NSObject
```

## Mentions

- [Declaring complications for your app](./declaring-complications-for-your-app.md)
- [Creating a timeline entry](./creating-a-timeline-entry.md)

#### Overview

Use complication descriptors to define the different types of complications that your app supports. Each descriptor provides a unique identifier for the complication, and the list of families that the complication supports. ClockKit defines the available families using the [`CLKComplicationFamily`](./clkcomplicationfamily.md) enumeration, while your app can define as many identifiers as it needs. Each unique [`identifier`](./clkcomplication/identifier.md) within your app represents a separate complication in the complication picker. For example, a weather app may have separate descriptors for `Condition`, `Temperature`, and `Precipitation.`

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

When dynamically creating identifiers, consider using the descriptor’s [`userInfo`](./clkcomplicationdescriptor/userinfo.md) property to contain any additional information your app needs to create timeline entries for the complication. In the above example, the weather app adds the `myCityIDKey` and `myTypeIdentifierKey` `keys` so that it can access the city and weather data type without parsing the `identifier` string.

## Topics

### Creating descriptors
- [convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily])](./clkcomplicationdescriptor/init%28identifier,displayname,supportedfamilies%29.md)
  Returns a new complication descriptor.
- [convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily], userActivity: NSUserActivity)](./clkcomplicationdescriptor/init%28identifier,displayname,supportedfamilies,useractivity%29.md)
  Returns a new complication descriptor with an associated user activity.
- [convenience init(identifier: String, displayName: String, supportedFamilies: [CLKComplicationFamily], userInfo: [AnyHashable : Any])](./clkcomplicationdescriptor/init%28identifier,displayname,supportedfamilies,userinfo%29.md)
  Returns a new complication descriptor with an associated dictionary of user data.
- [- initWithIdentifier:displayName:supportedFamilies:](./clkcomplicationdescriptor/initwithidentifier_displayname_supportedfamilies_.md)
  Returns a new complication descriptor.
- [- initWithIdentifier:displayName:supportedFamilies:userActivity:](./clkcomplicationdescriptor/initwithidentifier_displayname_supportedfamilies_useractivity_.md)
  Returns a new complication descriptor with an associated user activity.
- [- initWithIdentifier:displayName:supportedFamilies:userInfo:](./clkcomplicationdescriptor/initwithidentifier_displayname_supportedfamilies_userinfo_.md)
  Returns a new complication descriptor with an associated user info dictionary.
### Accessing the descriptor’s data
- [var identifier: String](./clkcomplicationdescriptor/identifier.md)
  A string that uniquely identifies the descriptor.
- [var displayName: String](./clkcomplicationdescriptor/displayname.md)
  A localized string that identifies complications from the descriptor to the user.
- [var supportedFamilies: [CLKComplicationFamily]](./clkcomplicationdescriptor/supportedfamilies-4ckbx.md)
  The families that support this type of complication.
- [var userActivity: NSUserActivity?](./clkcomplicationdescriptor/useractivity.md)
  A user activity object that represents the state of the app at a moment in time.
- [var userInfo: [AnyHashable : Any]?](./clkcomplicationdescriptor/userinfo.md)
  A dictionary of data that your data source can use to generate timeline entries.
- [supportedFamilies](./clkcomplicationdescriptor/supportedfamilies-50ink.md)
  The families that support this type of complication.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Migration Support
- [Migrating ClockKit complications to WidgetKit](../WidgetKit/converting-a-clockkit-app.md)
  Leverage WidgetKit’s API to create watchOS complications using SwiftUI.
- [protocol CLKComplicationDataSource](./clkcomplicationdatasource.md)
  A protocol that provides ClockKit with information about your complication.
- [let CLKDefaultComplicationIdentifier: String](./clkdefaultcomplicationidentifier.md)
  An identifier representing a default complication.
- [CLKAllComplicationFamilies](./clkallcomplicationfamilies.md)
  Returns an array containing all possible values of the complication family enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor)*