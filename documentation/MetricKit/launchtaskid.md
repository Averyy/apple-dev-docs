# LaunchTaskID

**Framework**: MetricKit  
**Kind**: struct

An identifier for a task measured as part of an extended app launch.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct LaunchTaskID
```

#### Discussion

`LaunchTaskID` is `RawRepresentable` and `ExpressibleByStringLiteral`. You can pass a string literal directly as the `id` argument to [`trackLaunchTask(id:onTrackingError:_:)`](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-48k2s.md) or [`trackLaunchTask(id:onTrackingError:_:)`](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-jnu1.md):

```swift
await manager.trackLaunchTask(id: "initial-data-load") {
    await loadInitialData()
}
```

Choose unique, descriptive names for each task you track. The system uses the ID to associate measurements with the specific work you perform during launch.

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct StateReportingDomain](statereportingdomain.md)
  A value that identifies a reporting scope for segmenting metric data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/launchtaskid)*