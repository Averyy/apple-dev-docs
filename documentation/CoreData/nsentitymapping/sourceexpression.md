# sourceExpression

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The source expression for the entity mapping.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sourceExpression: NSExpression? { get set }
```

```objc
@property (strong, nullable) NSExpression * sourceExpression;
```

## Discussion

The source expression is used to obtain the collection of managed objects to process through the mapping. The expression can be a fetch request expression, or any other expression that evaluates to a collection.

## See Also

### Managing Source Information
- [var sourceEntityName: String?](./sourceentityname.md)
  The source entity name for the entity mapping.
- [var sourceEntityVersionHash: Data?](./sourceentityversionhash.md)
  The version hash of the source entity for the entity mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymapping/sourceexpression)*