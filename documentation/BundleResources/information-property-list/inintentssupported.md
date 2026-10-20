# INIntentsSupported

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The names of the intent classes your app handles directly.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Details

- **Name**: `INIntentsSupported` (Intents eligible for in-app handling)
- **Type**: array of string 

#### Discussion

Provide the class name of each [`INIntent`](https://developer.apple.com/documentation/intents/inintent) subclass your app can handle. To specify this information in Xcode, add the class names in the Supported Intents section of your app target in the Project Editor.

For more information on handling intents in your app, see [`application(_:handlerFor:)`](../../UIKit/uiapplicationdelegate/application%28_,handlerfor%29.md).

> 💡 **Tip**:  You can start handling an intent in your app even if you want to support the intent in iOS 13. List the intent in the Supported Intents sections for both the app target and the extension target. For an app running on iOS 13, the system routes the intent with [`handler(for:)`](https://developer.apple.com/documentation/intents/inintenthandlerproviding/handler(for:)), and for later iOS versions, it routes the intent with [`application(_:handlerFor:)`](../../UIKit/uiapplicationdelegate/application%28_,handlerfor%29.md).

## See Also

### Intents
- [INIntentsRestrictedWhileLocked](./inintentsrestrictedwhilelocked.md)
  The names of the intent classes your app can’t handle when the user locks the device.
- [INIntentsRestrictedWhileProtectedDataUnavailable](./inintentsrestrictedwhileprotecteddataunavailable.md)
  The names of the intent classes your app can’t handle when the user locks the device or the system blocks access to protected data.
- [INSupportedMediaCategories](./insupportedmediacategories.md)
  Types of media supported by your app’s media-playing intents.
- [NSFocusStatusUsageDescription](./nsfocusstatususagedescription.md)
  A message that tells people why your app requests access to a person’s focus status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/inintentssupported)*