# load(_:_:_:isolation:)

**Framework**: AVFoundation  
**Kind**: method

Loads two or more properties asynchronously and returns the values.

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
@backDeployed(before: macOS 16, iOS 19, tvOS 19, watchOS 12, visionOS 3)
func load<A, B, each C>(_ firstProperty: AVAsyncProperty<Self, A>, _ secondProperty: AVAsyncProperty<Self, B>, _ properties: repeat AVAsyncProperty<Self, each C>, isolation: isolated (any Actor)? = #isolation) async throws -> (A, B, repeat each C)
```

#### Return Value

The loaded properties in a tuple.

#### Discussion

See the [`load(_:isolation:)`](avasynchronouskeyvalueloading/load(_:isolation:).md) method for more information.

## Parameters

- `firstProperty`: A property to load.
- `secondProperty`: A second property to load.
- `properties`: Additional properties to load.
- `isolation`: The isolation context.

## See Also

- [func load<T>(AVAsyncProperty<Self, T>, isolation: isolated (any Actor)?) async throws -> T](avasynchronouskeyvalueloading/load(_:isolation:).md)
  Loads a property asynchronously and returns the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/load(_:_:_:isolation:))*