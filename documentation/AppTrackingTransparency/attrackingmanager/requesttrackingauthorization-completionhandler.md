# requestTrackingAuthorization(completionHandler:)

**Framework**: App Tracking Transparency  
**Kind**: method

Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func requestTrackingAuthorization() async -> ATTrackingManager.AuthorizationStatus
```

#### Discussion

This method requests authorization to access app-related data that the app can use to track the person or the device. In France, Germany, Italy, Poland, and Romania, the system presents a full-page sheet; otherwise, the system prompts the person with an alert.

#### Handle the Persons Response

When the person answers the prompt, the system calls the completion handler with a status object ([`ATTrackingManager.AuthorizationStatus`](attrackingmanager/authorizationstatus.md)) set to [`ATTrackingManager.AuthorizationStatus.authorized`](attrackingmanager/authorizationstatus/authorized.md) or [`ATTrackingManager.AuthorizationStatus.denied`](attrackingmanager/authorizationstatus/denied.md), depending on the person’s response.

The status is [`ATTrackingManager.AuthorizationStatus.notDetermined`](attrackingmanager/authorizationstatus/notdetermined.md) if the system dismisses the prompt without a decision from the person; in this scenario, your app needs to call the method again to receive an authorization answer from the person.

In some cases, the system doesn’t display the prompt and instead runs your completion handler immediately. The system doesn’t prompt the person when:

- Tracking is restricted for the device; in this case, the [`trackingAuthorizationStatus`](attrackingmanager/trackingauthorizationstatus.md) is [`ATTrackingManager.AuthorizationStatus.restricted`](attrackingmanager/authorizationstatus/restricted.md) regardless of whether the system has shown the person the prompt.
- The person disables “Allow Apps to Request to Track” (called “Allow Apps to Request to Link Your Activity Across Companies” in the European Union) in Settings > Privacy & Security > Tracking.
- An existing permission request is pending.
- Your code invokes this method through an app extension.
- The app’s state is a value other than `UIApplicationStateActive`.

#### Prompt Again After a Year

In the European Union, if a person answers the prompt, the system notes the date and doesn’t allow the prompt to display again until a year passes. You can make an additional request after a year whether the person approves or denies your app’s previous tracking request, unless the person disables tracking in Settings > Privacy & Security > Tracking.

#### Configure the Apps Target Properties

To use this method, add the [`NSUserTrackingUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsusertrackingusagedescription) key to your app’s target properties in Xcode.

In France, Germany, Italy, Poland, and Romania, the full-page sheet displays the [`NSUserTrackingMarkdownUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsusertrackingmarkdownusagedescription) string with support for rich-text elements if you include it in your app’s target configuration in Xcode.

## See Also

- [class func requestTrackingAuthorization(usingExpandedInterface: Bool, additionalInformationAction: (() -> Void)?, completionHandler: (ATTrackingManager.AuthorizationStatus) -> Void)](attrackingmanager/requesttrackingauthorization(usingexpandedinterface:additionalinformationaction:completionhandler:).md)
  Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.
- [NSUserTrackingMarkdownUsageDescription](../bundleresources/information-property-list/nsusertrackingmarkdownusagedescription.md)
  A message that explains the purpose for accessing data that an application can use to track a person or device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:))*