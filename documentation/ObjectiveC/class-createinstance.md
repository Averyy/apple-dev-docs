# class_createInstance(_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Creates an instance of a class, allocating memory for the class in the default malloc memory zone.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func class_createInstance(_ cls: AnyClass?, _ extraBytes: Int) -> Any?
```

#### Return Value

An instance of the class `cls`.

## Parameters

- `cls`: The class that you want to allocate an instance of.
- `extraBytes`: An integer indicating the number of extra bytes to allocate. The additional bytes can be used to store additional instance variables beyond those defined in the class definition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/class_createinstance(_:_:))*