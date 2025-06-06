# PrimitivePlottableProtocol

**Framework**: Swift Charts  
**Kind**: protocol

A type that represents the primitive plottable types supported by the framework. Don’t use this type directly.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol PrimitivePlottableProtocol : Plottable where Self == Self.PrimitivePlottable
```

#### Overview

A primitive plottable type is a numeric type like a [`Float`](https://developer.apple.com/documentation/Swift/Float) or [`UInt32`](https://developer.apple.com/documentation/Swift/UInt32) for quantitative values, [`Date`](https://developer.apple.com/documentation/Foundation/Date) for temporal values, or [`String`](https://developer.apple.com/documentation/Swift/String) for categorical values.

Primitive plottable types conform to the [`Plottable`](plottable.md) protocol.

## Relationships

### Inherits From
- [Plottable](plottable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/primitiveplottableprotocol)*