# mainParticipantConfiguration

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

The app-specific configuration for the app that invokes the assessment.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var mainParticipantConfiguration: AEAssessmentParticipantConfiguration { get }
```

```objc
@property (nonatomic, strong, readonly) AEAssessmentParticipantConfiguration * mainParticipantConfiguration;
```

## Discussion

Use this property to get and customize the app-specific configuration that’s applied to your own app. For example, you can set the [`allowsNetworkAccess`](../aeassessmentparticipantconfiguration/allowsnetworkaccess.md) property for your own app:

**Swift**:

```swift
let config = AEAssessmentConfiguration()
config.mainParticipantConfiguration.allowsNetworkAccess = false
```

**Objective-C**:

```objc
AEAssessmentConfiguration *config = [[AEAssessmentConfiguration alloc] init];
[config mainParticipantConfiguration].allowsNetworkAccess = NO;
```

## See Also

### Allowing access to other apps
- [var configurationsByApplication: [AEAssessmentApplication : AEAssessmentParticipantConfiguration]](./configurationsbyapplication.md)
  The collection of apps available during an assessment, along with their associated configurations.
- [class AEAssessmentApplication](../aeassessmentapplication.md)
  A representation of an app that users can access during an assessment.
- [class AEAssessmentParticipantConfiguration](../aeassessmentparticipantconfiguration.md)
  Configuration information for an app that’s available during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/mainparticipantconfiguration)*