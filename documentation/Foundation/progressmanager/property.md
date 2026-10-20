# ProgressManager.Property

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

A type that conveys additional task-specific information on progress.

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
protocol Property : SendableMetatype
```

#### Overview

The `Property` protocol defines custom properties that can be associated with progress tracking. These properties allow you to store and aggregate additional information alongside the standard progress metrics such as `totalCount` and `completedCount`.

## Topics

### Associated Types
- [associatedtype Summary : Equatable, Sendable](./property/summary.md)
  The type used for aggregated summaries of this property.
- [associatedtype Value : Equatable, Sendable](./property/value.md)
  The type used for individual values of this property.
### Type Properties
- [static var defaultSummary: Self.Summary](./property/defaultsummary.md)
  The default summary value for this property type.
- [static var defaultValue: Self.Value](./property/defaultvalue.md)
  The default value to return when property is not set to a specific value.
- [static var key: String](./property/key.md)
  A unique identifier for this property type.
### Type Methods
- [static func finalSummary(Self.Summary, Self.Summary) -> Self.Summary](./property/finalsummary%28_,_%29.md)
  Determines how to handle summary data when a progress manager is deinitialized.
- [static func merge(Self.Summary, Self.Summary) -> Self.Summary](./property/merge%28_,_%29.md)
  Merges two summary values into a single combined summary.
- [static func reduce(into: inout Self.Summary, value: Self.Value)](./property/reduce%28into,value%29.md)
  Reduces a property value into an accumulating summary.

## Relationships

### Inherits From
- [SendableMetatype](../../Swift/sendablemetatype.md)
### Conforming Types
- [ProgressManager.Properties.CompletedByteCount](./properties/completedbytecount-swift.enum.md)
- [ProgressManager.Properties.CompletedFileCount](./properties/completedfilecount-swift.enum.md)
- [ProgressManager.Properties.EstimatedTimeRemaining](./properties/estimatedtimeremaining-swift.enum.md)
- [ProgressManager.Properties.Throughput](./properties/throughput-swift.enum.md)
- [ProgressManager.Properties.TotalByteCount](./properties/totalbytecount-swift.enum.md)
- [ProgressManager.Properties.TotalFileCount](./properties/totalfilecount-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/property)*