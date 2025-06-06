# load(_:_:_:_:_:_:_:_:)

**Framework**: AVFoundation  
**Kind**: method

Loads eight properties asynchronously and returns the values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func load<A, B, C, D, E, F, G, H>(_ propertyA: AVAsyncProperty<Self, A>, _ propertyB: AVAsyncProperty<Self, B>, _ propertyC: AVAsyncProperty<Self, C>, _ propertyD: AVAsyncProperty<Self, D>, _ propertyE: AVAsyncProperty<Self, E>, _ propertyF: AVAsyncProperty<Self, F>, _ propertyG: AVAsyncProperty<Self, G>, _ propertyH: AVAsyncProperty<Self, H>) async throws -> (A, B, C, D, E, F, G, H)
```

#### Return Value

The loaded properties in a tuple.

#### Discussion

See the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method for more information.

## Parameters

- `propertyA`: A property to load.
- `propertyB`: A second property to load.
- `propertyC`: A third property to load.
- `propertyD`: A fourth property to load.
- `propertyE`: A fifth property to load.
- `propertyF`: A sixth property to load.
- `propertyG`: A seventh property to load.
- `propertyH`: An eighth property to load.

## See Also

- [func load<T>(AVAsyncProperty<Self, T>) async throws -> T](avasynchronouskeyvalueloading/load(_:).md)
  Loads a property asynchronously and returns the value.
- [func load<A, B>(AVAsyncProperty<Self, A>, AVAsyncProperty<Self, B>) async throws -> (A, B)](avasynchronouskeyvalueloading/load(_:_:).md)
  Loads two properties asynchronously and returns the values.
- [func load<A, B, C>(AVAsyncProperty<Self, A>, AVAsyncProperty<Self, B>, AVAsyncProperty<Self, C>) async throws -> (A, B, C)](avasynchronouskeyvalueloading/load(_:_:_:).md)
  Loads three properties asynchronously and returns the values.
- [func load<A, B, C, D>(AVAsyncProperty<Self, A>, AVAsyncProperty<Self, B>, AVAsyncProperty<Self, C>, AVAsyncProperty<Self, D>) async throws -> (A, B, C, D)](avasynchronouskeyvalueloading/load(_:_:_:_:).md)
  Loads four properties asynchronously and returns the values.
- [func load<A, B, C, D, E>(AVAsyncProperty<Self, A>, AVAsyncProperty<Self, B>, AVAsyncProperty<Self, C>, AVAsyncProperty<Self, D>, AVAsyncProperty<Self, E>) async throws -> (A, B, C, D, E)](avasynchronouskeyvalueloading/load(_:_:_:_:_:).md)
  Loads five properties asynchronously and returns the values.
- [func load<A, B, C, D, E, F>(AVAsyncProperty<Self, A>, AVAsyncProperty<Self, B>, AVAsyncProperty<Self, C>, AVAsyncProperty<Self, D>, AVAsyncProperty<Self, E>, AVAsyncProperty<Self, F>) async throws -> (A, B, C, D, E, F)](avasynchronouskeyvalueloading/load(_:_:_:_:_:_:).md)
  Loads six properties asynchronously and returns the values.
- [func load<A, B, C, D, E, F, G>(AVAsyncProperty<Self, A>, AVAsyncProperty<Self, B>, AVAsyncProperty<Self, C>, AVAsyncProperty<Self, D>, AVAsyncProperty<Self, E>, AVAsyncProperty<Self, F>, AVAsyncProperty<Self, G>) async throws -> (A, B, C, D, E, F, G)](avasynchronouskeyvalueloading/load(_:_:_:_:_:_:_:).md)
  Loads seven properties asynchronously and returns the values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/load(_:_:_:_:_:_:_:_:))*