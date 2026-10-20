# init(SCNMatrix4:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a value object that contains the specified SceneKit 4 x 4 matrix.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(SCNMatrix4 v: SCNMatrix4)
```

```swift
init(scnMatrix4 v: SCNMatrix4)
```

```objc
+ (NSValue *) valueWithSCNMatrix4:(SCNMatrix4) v;
```

#### Return Value

A new value object that contains the matrix information.

## Parameters

- `v`: The value for the new object.

## See Also

### Related Documentation
- [typealias SCNMatrix4](../../SceneKit/scnmatrix4-swift.typealias.md)
  A representation of a 4 x 4 matrix.
### Working with SceneKit Vector and Matrix Values
- [init(SCNVector3: SCNVector3)](./init%28scnvector3%29.md)
  Creates a value object that contains the specified three-element SceneKit vector.
- [init(SCNVector4: SCNVector4)](./init%28scnvector4%29.md)
  Creates a value object that contains the specified four-element SceneKit vector.
- [var scnVector3Value: SCNVector3](./scnvector3value.md)
  The three-element Scene Kit vector representation of the value.
- [var scnVector4Value: SCNVector4](./scnvector4value.md)
  The four-element Scene Kit vector representation of the value.
- [var scnMatrix4Value: SCNMatrix4](./scnmatrix4value.md)
  The Scene Kit 4 x 4 matrix representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(scnmatrix4:))*