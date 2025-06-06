# derivationExpression

**Framework**: Core Data  
**Kind**: property

An expression for generating derived data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var derivationExpression: NSExpression? { get set }
```

#### Discussion

When using derived attributes in an SQL store, this expression should be

- a keypath expression (including @operation components)

a function expression using one of the predefined functions defined in [`NSExpression`](https://developer.apple.com/documentation/Foundation/NSExpression)

Any keypaths used in the expression must be accessible from the entity on which the derived attribute is specified.

If you try to add a store to a coordinator whose model contains derived attributes of a type not supported by the store, the add fails and throws an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsderivedattributedescription/derivationexpression)*