# init(_:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a multiarray from a shaped array.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
convenience init<ShapedArray>(_ shapedArray: ShapedArray) where ShapedArray : MLShapedArrayProtocol
```

**Other overloads**:

```swift
convenience init<C>(_ data: C) throws where C : Collection, C.Element : FixedWidthInteger
```

```swift
convenience init<C>(_ data: C) throws where C : Collection, C.Element == Double
```

```swift
convenience init<C>(_ data: C) throws where C : Collection, C.Element == Float
```

## Parameters

- `shapedArray`: An [`MLShapedArray`](../mlshapedarray.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(_:)-wk41)*