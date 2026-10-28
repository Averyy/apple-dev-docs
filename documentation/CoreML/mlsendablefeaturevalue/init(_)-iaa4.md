# init(_:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a feature value containing a 16-bit floating-point value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(_ value: Float16)
```

**Other overloads**:

```swift
init(_ value: Double)
```

```swift
init(_ value: Float)
```

```swift
init(_ value: Int)
```

```swift
init(_ value: Int32)
```

```swift
init(_ value: String)
```

```swift
init(_ value: [Int : Double])
```

```swift
init(_ value: [Int : Int])
```

```swift
init(_ value: [String : Double])
```

```swift
init(_ value: [String : Int])
```

```swift
init(_ value: [String])
```

```swift
init<Scalar>(_ value: MLShapedArray<Scalar>) where Scalar : MLShapedArrayScalar
```

```swift
init?(_ value: MLFeatureValue)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlsendablefeaturevalue/init(_:)-iaa4)*