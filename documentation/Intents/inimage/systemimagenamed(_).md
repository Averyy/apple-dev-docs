# systemImageNamed(_:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Returns an image object that contains the specified system symbol image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class func systemImageNamed(_ systemImageName: String) -> Self
```

```objc
+ (instancetype) systemImageNamed:(NSString *) systemImageName;
```

## Return Value

An object that contains the specified symbol image. If `systemImageName` is invalid, the system passes `nil` to the completion handler of [`fetchUIImage(completion:)`](./fetchuiimage%28completion%29.md).

## Parameters

- `systemImageName`: The name of the system symbol image. Use the [SF Symbols](https://developer.apple.com/sf-symbols) app to look up the names of system symbol images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inimage/systemimagenamed(_:))*