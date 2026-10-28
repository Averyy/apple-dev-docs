# type

**Framework**: AVRouting  
**Kind**: property  
**Role**: Instance Property

A type with an identifier that matches a value in the app’s configuration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var type: UTType { get set }
```

```objc
@property (nonatomic, copy) UTType * type;
```

## Discussion

Provide a `UTType` symbol name and description in your app’s `Info.plist` file.

## See Also

### Configuring an item
- [var overrideTitle: String?](./overridetitle.md)
  A string to use to override the title of the item’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingactionitem/type)*