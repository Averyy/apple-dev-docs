# ProgressManager

**Framework**: Foundation  
**Kind**: class

An object that conveys ongoing progress to the user for a specified task.

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
final class ProgressManager
```

## Topics

### Protocols
- [ProgressManager.Property](progressmanager/property.md)
  A type that conveys additional task-specific information on progress.
### Initializers
- [convenience init(totalCount: Int?)](progressmanager/init(totalcount:).md)
  Initializes `self` with `totalCount`.
### Instance Properties
- [var completedCount: Int](progressmanager/completedcount.md)
  The completed units of work.
- [var fractionCompleted: Double](progressmanager/fractioncompleted.md)
  The proportion of work completed. This takes into account the fraction completed in its children instances if children are present. If `self` is indeterminate, the value will be 0.0.
- [var isFinished: Bool](progressmanager/isfinished.md)
  The state of completion of work. If `completedCount` >= `totalCount`, the value will be `true`.
- [var isIndeterminate: Bool](progressmanager/isindeterminate.md)
  The state of initialization of `totalCount`. If `totalCount` is `nil`, the value will be `true`.
- [var reporter: ProgressReporter](progressmanager/reporter.md)
  A `ProgressReporter` instance, used for providing read-only observation of progress updates or composing into other `ProgressManager`s.
- [var totalCount: Int?](progressmanager/totalcount.md)
  The total units of work.
### Instance Methods
- [func assign(count: Int, to: Progress)](progressmanager/assign(count:to:)-87zdf.md)
  Adds a Foundation’s `Progress` instance as a child which constitutes a certain `count` of `self`’s `totalCount`.
- [func assign(count: Int, to: ProgressReporter)](progressmanager/assign(count:to:)-98a77.md)
  Adds a `ProgressReporter` as a child, with its progress representing a portion of `self`’s progress.
- [func complete(count: Int)](progressmanager/complete(count:).md)
  Increases `completedCount` by `count`.
- [func setCounts((inout Int, inout Int?) -> Void)](progressmanager/setcounts(_:).md)
- [func subprogress(assigningCount: Int) -> Subprogress](progressmanager/subprogress(assigningcount:).md)
  Returns a `Subprogress` representing a portion of `self` which can be passed to any method that reports progress.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> P.Summary](progressmanager/summary(of:)-3kyy8.md)
  Returns a summary for a custom URL property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> P.Summary](progressmanager/summary(of:)-3r60q.md)
  Returns a summary for a custom integer property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> P.Summary](progressmanager/summary(of:)-3voby.md)
  Returns a summary for a custom double property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> P.Summary](progressmanager/summary(of:)-73lzs.md)
  Returns a summary for a custom duration property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> P.Summary](progressmanager/summary(of:)-7jb53.md)
  Returns a summary for a custom unsigned integer property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> P.Summary](progressmanager/summary(of:)-bfr7.md)
  Returns a summary for a custom string property across the progress subtree.
- [func summary<P>(of: KeyPath<ProgressManager.Properties, P.Type>) -> P.Summary](progressmanager/summary(of:)-txm5.md)
  Returns a summary for a custom unsigned integer property across the progress subtree.
### Subscripts
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> Int](progressmanager/subscript(dynamicmember:)-1qb7p.md)
  Gets or sets custom integer properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> String?](progressmanager/subscript(dynamicmember:)-5rh0j.md)
  Gets or sets custom string properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> Duration](progressmanager/subscript(dynamicmember:)-5rw99.md)
  Gets or sets custom duration properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> P.Value](progressmanager/subscript(dynamicmember:)-62at9.md)
  Gets or sets custom double properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> UInt64](progressmanager/subscript(dynamicmember:)-7h16n.md)
  Gets or sets custom unsigned integer properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> URL?](progressmanager/subscript(dynamicmember:)-7r4v2.md)
  Gets or sets custom URL properties.
- [subscript<P>(dynamicMember _: KeyPath<ProgressManager.Properties, P.Type>) -> UInt64](progressmanager/subscript(dynamicmember:)-8tb3b.md)
  Gets or sets custom unsigned integer properties.
### Enumerations
- [ProgressManager.Properties](progressmanager/properties.md)
### Default Implementations
- [CustomDebugStringConvertible Implementations](progressmanager/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](progressmanager/customstringconvertible-implementations.md)
- [Equatable Implementations](progressmanager/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Observable](../observation/observable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager)*