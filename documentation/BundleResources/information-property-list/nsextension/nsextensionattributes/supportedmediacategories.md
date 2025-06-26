# SupportedMediaCategories

**Framework**: Bundle Resources  
**Kind**: typealias

Types of media supported by an app extension’s media-playing intents.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

#### Discussion

Specify one or more media categories to allow Siri to invoke your app’s intent handling when a user asks to play media. Use `INMediaCategoryGeneral` for media that doesn’t fit into any of the other categories, like white noise or sound effects.

To specify this information in Xcode, add doc://com.apple.documentation/documentation/sirikit/inplaymediaintent to your extension’s list of Supported Intents. Then select the relevant media types in the list that appears.

## See Also

- [IntentsSupported](information-property-list/nsextension/intentssupported.md)
  The names of the intents that an extension supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionattributes/supportedmediacategories)*