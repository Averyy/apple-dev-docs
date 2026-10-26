# identity

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the intent in the document.

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
@property (readonly) NSInteger identity;
```

#### Discussion

Use the value in this property to disambiguate attributes that apply to contiguous text. For example, you might use it to differentiate between two headers in a row with the same level.

## See Also

### Getting the intent identity
- [intentKind](./intentkind.md)
  The type of the intent.
- [parentIntent](./parentintent.md)
  The parent of the current intent.
- [- isEquivalentToPresentationIntent:](./isequivalenttopresentationintent_.md)
  Returns a Boolean value that indicates whether the current intent is equivalent to the specified intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspresentationintent/identity)*