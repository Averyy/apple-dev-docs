# load(_:isolation:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Loads a property asynchronously and returns the value.

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
@backDeployed(before: macOS 26.0, iOS 26.0, tvOS 26.0, watchOS 26.0, visionOS 26.0)
func load<T>(_ property: AVAsyncProperty<Self, T>, isolation: isolated (any Actor)? = #isolation) async throws -> T
```

## Mentions

- [Loading media data asynchronously](../loading-media-data-asynchronously.md)

#### Return Value

The loaded property value.

#### Discussion

Call this method from an asynchronous context to load the value of one or more media properties. The method returns a single result if you load one property value, and returns a tuple if you load multiple properties (up to eight) at the same time.

To load a property, pass one or more [`AVAsyncProperty`](../avasyncproperty.md) constants to this method as shown below.

```swift
// Load an asset's list of tracks.
let tracks = try await asset.load(.tracks)
        
// Load an asset's suitability for playback and export.
let (isPlayable, isExportable) = try await asset.load(.isPlayable, .isExportable)
```

## Parameters

- `property`: A property to load.
- `isolation`: The isolation context.

## See Also

### Loading property values
- [func load<A, B, each C>(AVAsyncProperty<Self, A>, AVAsyncProperty<Self, B>, repeat AVAsyncProperty<Self, each C>, isolation: isolated (any Actor)?) async throws -> (A, B, repeat each C)](./load%28_,_,_,isolation%29.md)
  Loads two or more properties asynchronously and returns the values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/load(_:isolation:))*