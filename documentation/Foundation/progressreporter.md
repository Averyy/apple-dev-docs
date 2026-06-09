# ProgressReporter

**Framework**: Foundation  
**Kind**: class

ProgressReporter is a wrapper for ProgressManager that carries information about ProgressManager.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@dynamicMemberLookup
final class ProgressReporter
```

#### Overview

It is read-only and can be added as a child of another ProgressManager.

## Topics

### Instance Properties
- [var completedCount: Int](progressreporter/completedcount.md)
  The completed units of work. If `self` is indeterminate, the value will be 0.
- [var debugDescription: String](progressreporter/debugdescription.md)
  A textual representation of the progress reporter suitable for debugging.
- [var description: String](progressreporter/description.md)
  A textual representation of the progress reporter.
- [var fractionCompleted: Double](progressreporter/fractioncompleted.md)
  The proportion of work completed. This takes into account the fraction completed in its children instances if children are present. If `self` is indeterminate, the value will be 0.
- [var isFinished: Bool](progressreporter/isfinished.md)
  The state of completion of work. If `completedCount` >= `totalCount`, the value will be `true`.
- [var isIndeterminate: Bool](progressreporter/isindeterminate.md)
  The state of initialization of `totalCount`. If `totalCount` is `nil`, the value will be `true`.
- [var totalCount: Int?](progressreporter/totalcount.md)
  The total units of work.
### Instance Methods
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> [UInt64]](progressreporter/summary(of:)-2qbq7.md)
  Returns a summary for the specified unsigned integer array property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> Double](progressreporter/summary(of:)-4lsh2.md)
  Returns a summary for the specified double property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> [String?]](progressreporter/summary(of:)-5klzp.md)
  Returns a summary for the specified string property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> [URL?]](progressreporter/summary(of:)-6x2a5.md)
  Returns a summary for the specified URL property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> Int](progressreporter/summary(of:)-7u7bg.md)
  Returns a summary for the specified integer property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> UInt64](progressreporter/summary(of:)-7xg8c.md)
  Returns a summary for the specified unsigned integer property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> Duration](progressreporter/summary(of:)-vlsj.md)
  Returns a summary for the specified duration property across the progress subtree.
### Subscripts
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> String?](progressreporter/subscript(dynamicmember:)-114si.md)
  Gets or sets custom string properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> UInt64](progressreporter/subscript(dynamicmember:)-1ubk6.md)
  Gets or sets custom unsigned integer properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> UInt64](progressreporter/subscript(dynamicmember:)-45eys.md)
  Gets or sets custom unsigned integer properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> URL?](progressreporter/subscript(dynamicmember:)-84opo.md)
  Gets or sets custom URL properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> P.Value](progressreporter/subscript(dynamicmember:)-9fd3u.md)
  Gets or sets custom double properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> Int](progressreporter/subscript(dynamicmember:)-9pcsi.md)
  Gets or sets custom integer properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> Duration](progressreporter/subscript(dynamicmember:)-cjlx.md)
  Gets or sets custom duration properties.
### Type Aliases
- [ProgressReporter.Property](progressreporter/property.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressreporter)*