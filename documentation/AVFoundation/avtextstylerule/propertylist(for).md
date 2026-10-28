# propertyList(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Converts one or more text style rules into a serializable property list object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func propertyList(for textStyleRules: [AVTextStyleRule]) -> Any
```

```objc
+ (id) propertyListForTextStyleRules:(NSArray<AVTextStyleRule *> *) textStyleRules;
```

## Return Value

A property-list object that you can pass to the [`PropertyListSerialization`](../../Foundation/propertylistserialization.md) serialization routines.

## Discussion

The property-list object returned by this method can be written to disk and stored persistently.

## Parameters

- `textStyleRules`: An array of `AVTextStyleRule` objects to write to the property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtextstylerule/propertylist(for:))*