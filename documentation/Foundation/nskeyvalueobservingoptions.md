# NSKeyValueObservingOptions

**Framework**: Foundation  
**Kind**: struct

The values that can be returned in a change dictionary.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct NSKeyValueObservingOptions
```

#### Overview

These constants are passed to [`addObserver(_:forKeyPath:options:context:)`](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/addobserver(_:forkeypath:options:context:)) and determine the values that are returned as part of the change dictionary passed to an [`observeValue(forKeyPath:of:change:context:)`](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/observevalue(forkeypath:of:change:context:)). You can pass `0` if you require no change dictionary values.

## Topics

### Constants
- [static var new: NSKeyValueObservingOptions](nskeyvalueobservingoptions/new.md)
  Indicates that the change dictionary should provide the new attribute value, if applicable.
- [static var old: NSKeyValueObservingOptions](nskeyvalueobservingoptions/old.md)
  Indicates that the change dictionary should contain the old attribute value, if applicable.
- [static var initial: NSKeyValueObservingOptions](nskeyvalueobservingoptions/initial.md)
  If specified, a notification should be sent to the observer immediately, before the observer registration method even returns.
- [static var prior: NSKeyValueObservingOptions](nskeyvalueobservingoptions/prior.md)
  Whether separate notifications should be sent to the observer before and after each change, instead of a single notification after the change.
### Initializers
- [init(rawValue: UInt)](nskeyvalueobservingoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [enum NSGrammaticalCase](nsgrammaticalcase.md)
- [enum NSGrammaticalDefiniteness](nsgrammaticaldefiniteness.md)
- [enum NSGrammaticalDetermination](nsgrammaticaldetermination.md)
- [enum NSGrammaticalPerson](nsgrammaticalperson.md)
- [enum NSGrammaticalPronounType](nsgrammaticalpronountype.md)
- [enum NSKeyValueChange](nskeyvaluechange.md)
  The kinds of changes that can be observed.
- [enum NSKeyValueSetMutationKind](nskeyvaluesetmutationkind.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions)*