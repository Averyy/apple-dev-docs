# ProgressReporter

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

ProgressReporter is a wrapper for ProgressManager that carries information about ProgressManager.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@dynamicMemberLookup
final class ProgressReporter
```

## Overview

It is read-only and can be added as a child of another ProgressManager.

## Topics

### Instance Properties
- [var completedCount: Int](./progressreporter/completedcount.md)
  The completed units of work. If `self` is indeterminate, the value will be 0.
- [var debugDescription: String](./progressreporter/debugdescription.md)
  A textual representation of the progress reporter suitable for debugging.
- [var description: String](./progressreporter/description.md)
  A textual representation of the progress reporter.
- [var fractionCompleted: Double](./progressreporter/fractioncompleted.md)
  The proportion of work completed. This takes into account the fraction completed in its children instances if children are present. If `self` is indeterminate, the value will be 0.
- [var isFinished: Bool](./progressreporter/isfinished.md)
  The state of completion of work. If `completedCount` >= `totalCount`, the value will be `true`.
- [var isIndeterminate: Bool](./progressreporter/isindeterminate.md)
  The state of initialization of `totalCount`. If `totalCount` is `nil`, the value will be `true`.
- [var totalCount: Int?](./progressreporter/totalcount.md)
  The total units of work.
### Instance Methods
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> [UInt64]](./progressreporter/summary%28of%29-2qbq7.md)
  Returns a summary for the specified unsigned integer array property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> Double](./progressreporter/summary%28of%29-4lsh2.md)
  Returns a summary for the specified double property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> [String?]](./progressreporter/summary%28of%29-5klzp.md)
  Returns a summary for the specified string property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> [URL?]](./progressreporter/summary%28of%29-6x2a5.md)
  Returns a summary for the specified URL property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> Int](./progressreporter/summary%28of%29-7u7bg.md)
  Returns a summary for the specified integer property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> UInt64](./progressreporter/summary%28of%29-7xg8c.md)
  Returns a summary for the specified unsigned integer property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> Duration](./progressreporter/summary%28of%29-vlsj.md)
  Returns a summary for the specified duration property across the progress subtree.
### Subscripts
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> String?](./progressreporter/subscript%28dynamicmember%29-114si.md)
  Gets or sets custom string properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> UInt64](./progressreporter/subscript%28dynamicmember%29-1ubk6.md)
  Gets or sets custom unsigned integer properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> UInt64](./progressreporter/subscript%28dynamicmember%29-45eys.md)
  Gets or sets custom unsigned integer properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> URL?](./progressreporter/subscript%28dynamicmember%29-84opo.md)
  Gets or sets custom URL properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> P.Value](./progressreporter/subscript%28dynamicmember%29-9fd3u.md)
  Gets or sets custom double properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> Int](./progressreporter/subscript%28dynamicmember%29-9pcsi.md)
  Gets or sets custom integer properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> Duration](./progressreporter/subscript%28dynamicmember%29-cjlx.md)
  Gets or sets custom duration properties.
### Type Aliases
- [ProgressReporter.Property](./progressreporter/property.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Observable](../Observation/observable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressreporter)*