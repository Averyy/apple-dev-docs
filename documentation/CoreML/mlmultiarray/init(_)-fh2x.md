# init(_:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a multiarray from a collection of floats.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init<C>(_ data: C) throws where C : Collection, C.Element == Float
```

**Other overloads**:

```swift
convenience init<C>(_ data: C) throws where C : Collection, C.Element : FixedWidthInteger
```

```swift
convenience init<C>(_ data: C) throws where C : Collection, C.Element == Double
```

```swift
convenience init<ShapedArray>(_ shapedArray: ShapedArray) where ShapedArray : MLShapedArrayProtocol
```

## Discussion

Use this initializer to create a multiarray from a collection of [`Float`](../../Swift/float.md) values, such as an array.

```swift
let floats: [Float] = [1.41, 1.73, 2.72, 3.14]
let floatMultiarray = try MLMultiArray(floats)
```

## Parameters

- `data`: A [`Collection`](../../Swift/collection.md) of [`Float`](../../Swift/float.md) values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(_:)-fh2x)*