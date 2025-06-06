# filtered(using:)

**Framework**: Foundation  
**Kind**: method

Evaluates a given predicate against each object in the receiving ordered set and returns a new ordered set containing the objects for which the predicate returns true.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func filtered(using p: NSPredicate) -> NSOrderedSet
```

#### Return Value

A new ordered set containing the objects in the receiving ordered set for which `p` returns true.

#### Discussion

For more details, see [`Predicate Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789).

## Parameters

- `p`: The predicate against which to evaluate the receiving ordered set’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/filtered(using:))*