# init(name:protectionClass:)

**Framework**: Core Spotlight  
**Kind**: init

Returns an on-device index with the specified name and data protection class.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
init(name: String, protectionClass: FileProtectionType?)
```

## Mentions

- [Adding your app’s content to Spotlight indexes](adding-your-app-s-content-to-spotlight-indexes.md)

#### Return Value

An index that can handle items within the specified protection class.

#### Discussion

Use this method to specify a protection class for an index. You can specify a default protection class for index items in the entitlements for your app.

## Parameters

- `name`: A name that pertains to your custom organization.
- `protectionClass`: The file protection class. Acceptable values are  ,  ,  , or  .

## See Also

- [class func `default`() -> Self](cssearchableindex/default.md)
  Returns the default on-device index.
- [init(name: String)](cssearchableindex/init(name:).md)
  Returns an on-device index with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/init(name:protectionclass:))*