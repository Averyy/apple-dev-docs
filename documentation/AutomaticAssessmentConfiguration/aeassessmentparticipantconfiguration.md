# AEAssessmentParticipantConfiguration

**Framework**: Automatic Assessment Configuration  
**Kind**: class

Configuration information for an app that’s available during an assessment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AEAssessmentParticipantConfiguration
```

#### Overview

Use an instance of this class to configure the properties of an app that you allow to run during an assessment. Associate the participant configuration with an app (an [`AEAssessmentApplication`](aeassessmentapplication.md) instance) when you call the `AEAssessmentConfiguration/setConfiguration(_:for:)` method of a session configuration.

## Topics

### Creating participant configuration instances
- [init()](aeassessmentparticipantconfiguration/init.md)
  Initializes an assessment participant configuration instance.
- [class func new() -> Self](aeassessmentparticipantconfiguration/new.md)
  Creates a new assessment participant configuration instance.
### Allowing network access
- [var allowsNetworkAccess: Bool](aeassessmentparticipantconfiguration/allowsnetworkaccess.md)
  A Boolean that indicates whether an app can access network resources during an assessment.
### Instance Properties
- [var allowedMenuItemLanguages: Set<Locale.Language>](aeassessmentparticipantconfiguration/allowedmenuitemlanguages.md)
  The set of languages for which allowed menu items have been configured.
- [var configurationInfo: [String : Any]](aeassessmentparticipantconfiguration/configurationinfo.md)
- [var isRequired: Bool](aeassessmentparticipantconfiguration/isrequired.md)
### Instance Methods
- [func allowedMenuItems(for: Locale.Language) -> Set<String>?](aeassessmentparticipantconfiguration/allowedmenuitems(for:).md)
  Returns the set of allowed menu item titles for the given language, or `nil` if no items have been configured for that language.
- [func setAllowedMenuItems(Set<String>?, for: Locale.Language)](aeassessmentparticipantconfiguration/setallowedmenuitems(_:for:).md)
  Sets the allowed menu item titles for the given language.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [var configurationsByApplication: [AEAssessmentApplication : AEAssessmentParticipantConfiguration]](aeassessmentconfiguration/configurationsbyapplication.md)
  The collection of apps available during an assessment, along with their associated configurations.
- [var mainParticipantConfiguration: AEAssessmentParticipantConfiguration](aeassessmentconfiguration/mainparticipantconfiguration.md)
  The app-specific configuration for the app that invokes the assessment.
- [class AEAssessmentApplication](aeassessmentapplication.md)
  A representation of an app that users can access during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentparticipantconfiguration)*