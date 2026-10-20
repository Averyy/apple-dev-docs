# LaunchTaskID

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

An identifier for a task measured as part of an extended app launch.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct LaunchTaskID
```

#### Discussion

`LaunchTaskID` is `RawRepresentable` and `ExpressibleByStringLiteral`. You can pass a string literal directly as the `id` argument to [`trackLaunchTask(id:onTrackingError:_:)`](./metricmanager/tracklaunchtask%28id,ontrackingerror,_%29-48k2s.md) or [`trackLaunchTask(id:onTrackingError:_:)`](./metricmanager/tracklaunchtask%28id,ontrackingerror,_%29-jnu1.md):

```swift
await manager.trackLaunchTask(id: "initial-data-load") {
    await loadInitialData()
}
```

Choose unique, descriptive names for each task you track. The system uses the ID to associate measurements with the specific work you perform during launch.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### App state reporting
- [struct StateReportingDomain](./statereportingdomain.md)
  A value that identifies a reporting scope for segmenting metric data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/launchtaskid)*