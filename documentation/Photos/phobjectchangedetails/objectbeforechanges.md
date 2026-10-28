# objectBeforeChanges

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

An object that reflects the original state of the asset or collection it represents.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var objectBeforeChanges: ObjectType { get }
```

```objc
@property (atomic, strong, readonly) ObjectType objectBeforeChanges;
```

## Discussion

This property’s value is the same object you passed to the [`changeDetailsForObject:`](../phchange/changedetailsforobject_.md) to request change details.

## See Also

### Getting the Changed Object
- [var objectAfterChanges: ObjectType?](./objectafterchanges.md)
  An object that reflects the current state of the asset or collection it represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phobjectchangedetails/objectbeforechanges)*