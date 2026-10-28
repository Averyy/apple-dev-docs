# init(_:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a multiarray from a collection of doubles.

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
convenience init<C>(_ data: C) throws where C : Collection, C.Element == Double
```

**Other overloads**:

```swift
convenience init<C>(_ data: C) throws where C : Collection, C.Element : FixedWidthInteger
```

```swift
convenience init<C>(_ data: C) throws where C : Collection, C.Element == Float
```

```swift
convenience init<ShapedArray>(_ shapedArray: ShapedArray) where ShapedArray : MLShapedArrayProtocol
```

## Discussion

Use this initializer to create a multiarray from a collection of [`Double`](../../Swift/double.md) values, such as an array.

```swift
let doubles: [Double] = [1.41, 1.73, 2.72, 3.14]
let doubleMultiarray = try MLMultiArray(doubles)
```

## Parameters

- `data`: A [`Collection`](../../Swift/collection.md) of [`Double`](../../Swift/double.md) values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(_:)-8bsfu)*