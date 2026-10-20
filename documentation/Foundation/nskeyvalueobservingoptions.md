# NSKeyValueObservingOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSKeyValueObservingOptions : NSUInteger;
```

#### Overview

These constants are passed to [`addObserver(_:forKeyPath:options:context:)`](../ObjectiveC/nsobject-swift.class/addobserver%28_,forkeypath,options,context%29.md) and determine the values that are returned as part of the change dictionary passed to an [`observeValue(forKeyPath:of:change:context:)`](../ObjectiveC/nsobject-swift.class/observevalue%28forkeypath,of,change,context%29.md). You can pass `0` if you require no change dictionary values.

## Topics

### Constants
- [static var new: NSKeyValueObservingOptions](./nskeyvalueobservingoptions/new.md)
  Indicates that the change dictionary should provide the new attribute value, if applicable.
- [static var old: NSKeyValueObservingOptions](./nskeyvalueobservingoptions/old.md)
  Indicates that the change dictionary should contain the old attribute value, if applicable.
- [static var initial: NSKeyValueObservingOptions](./nskeyvalueobservingoptions/initial.md)
  If specified, a notification should be sent to the observer immediately, before the observer registration method even returns.
- [static var prior: NSKeyValueObservingOptions](./nskeyvalueobservingoptions/prior.md)
  Whether separate notifications should be sent to the observer before and after each change, instead of a single notification after the change.
### Initializers
- [init(rawValue: UInt)](./nskeyvalueobservingoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Enumerations
- [enum NSGrammaticalCase](./nsgrammaticalcase.md)
- [enum NSGrammaticalDefiniteness](./nsgrammaticaldefiniteness.md)
- [enum NSGrammaticalDetermination](./nsgrammaticaldetermination.md)
- [enum NSGrammaticalPerson](./nsgrammaticalperson.md)
- [enum NSGrammaticalPronounType](./nsgrammaticalpronountype.md)
- [enum NSKeyValueChange](./nskeyvaluechange.md)
  The kinds of changes that can be observed.
- [enum NSKeyValueSetMutationKind](./nskeyvaluesetmutationkind.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions)*