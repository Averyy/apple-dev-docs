# ProgressManager.Property

**Framework**: Foundation  
**Kind**: protocol

A type that conveys additional task-specific information on progress.

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
protocol Property : SendableMetatype
```

#### Overview

The `Property` protocol defines custom properties that can be associated with progress tracking. These properties allow you to store and aggregate additional information alongside the standard progress metrics such as `totalCount` and `completedCount`.

## Topics

### Associated Types
- [associatedtype Summary : Equatable, Sendable](progressmanager/property/summary.md)
  The type used for aggregated summaries of this property.
- [associatedtype Value : Equatable, Sendable](progressmanager/property/value.md)
  The type used for individual values of this property.
### Type Properties
- [static var defaultSummary: Self.Summary](progressmanager/property/defaultsummary.md)
  The default summary value for this property type.
- [static var defaultValue: Self.Value](progressmanager/property/defaultvalue.md)
  The default value to return when property is not set to a specific value.
- [static var key: String](progressmanager/property/key.md)
  A unique identifier for this property type.
### Type Methods
- [static func finalSummary(Self.Summary, Self.Summary) -> Self.Summary](progressmanager/property/finalsummary(_:_:).md)
  Determines how to handle summary data when a progress manager is deinitialized.
- [static func merge(Self.Summary, Self.Summary) -> Self.Summary](progressmanager/property/merge(_:_:).md)
  Merges two summary values into a single combined summary.
- [static func reduce(into: inout Self.Summary, value: Self.Value)](progressmanager/property/reduce(into:value:).md)
  Reduces a property value into an accumulating summary.

## Relationships

### Inherits From
- [SendableMetatype](../swift/sendablemetatype.md)
### Conforming Types
- [ProgressManager.Properties.CompletedByteCount](progressmanager/properties/completedbytecount-swift.enum.md)
- [ProgressManager.Properties.CompletedFileCount](progressmanager/properties/completedfilecount-swift.enum.md)
- [ProgressManager.Properties.EstimatedTimeRemaining](progressmanager/properties/estimatedtimeremaining-swift.enum.md)
- [ProgressManager.Properties.Throughput](progressmanager/properties/throughput-swift.enum.md)
- [ProgressManager.Properties.TotalByteCount](progressmanager/properties/totalbytecount-swift.enum.md)
- [ProgressManager.Properties.TotalFileCount](progressmanager/properties/totalfilecount-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/property)*