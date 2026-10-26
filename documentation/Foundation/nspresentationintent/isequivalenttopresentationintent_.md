# isEquivalentToPresentationIntent:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the current intent is equivalent to the specified intent.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
- (BOOL) isEquivalentToPresentationIntent:(NSPresentationIntent *) other;
```

#### Return Value

[`true`](../../Swift/true.md) if the current intent is equivalent to the specified intent, or [`false`](../../Swift/false.md) if it isn’t.

#### Discussion

Two intents are equivalent if their attributes match. This method doesn’t consider the [`identity`](./identity.md) property of the intents when determining their equivalence.

## Parameters

- `other`: The other intent to use in the comparison.

## See Also

### Getting the intent identity
- [identity](./identity.md)
  A unique identifier for the intent in the document.
- [intentKind](./intentkind.md)
  The type of the intent.
- [parentIntent](./parentintent.md)
  The parent of the current intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspresentationintent/isequivalenttopresentationintent:)*