# Foundation Data Types

**Framework**: Foundation

This document describes the data types and constants found in the Foundation framework.

## Topics

### Classes
- [class NSKeyValueObservation](nskeyvalueobservation.md)
- [class NSKeyValueSharedObservers](nskeyvaluesharedobservers.md)
- [class NSKeyValueSharedObserversSnapshot](nskeyvaluesharedobserverssnapshot.md)
### Protocols
- [protocol DiscreteFormatStyle](discreteformatstyle.md)
- [protocol NSKeyValueObservingCustomization](nskeyvalueobservingcustomization.md)
  Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys
### Structures
- [struct AsyncCharacterSequence](asynccharactersequence.md)
  An asynchronous sequence of characters.
- [struct AsyncLineSequence](asynclinesequence.md)
  An asynchronous sequence of lines of text.
- [struct AsyncUnicodeScalarSequence](asyncunicodescalarsequence.md)
  An asychronous sequence of Unicode scalar values.
- [struct Expression](expression.md)
- [struct NSAttributedStringFormattingContextKey](nsattributedstringformattingcontextkey.md)
- [struct NSKeyValueChangeKey](nskeyvaluechangekey.md)
  The keys that can appear in the change dictionary.
- [struct NSKeyValueObservedChange](nskeyvalueobservedchange.md)
- [struct NSKeyValueOperator](nskeyvalueoperator.md)
  These constants define the available array operators. See [`Using Collection Operators`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/CollectionOperators.html) for more information.
- [struct PresentationIntent](presentationintent.md)
  A type that defines presentation intent for blocks of characters like paragraphs, lists, block quotes, and tables.
### Variables
- [let NSOperationNotSupportedForKeyException: String](nsoperationnotsupportedforkeyexception.md)
- [let NSURLSessionUploadTaskResumeData: String](nsurlsessionuploadtaskresumedata.md)
- [var kCFStringEncodingASCII: CFStringEncoding](kcfstringencodingascii.md)
### Macros
- [macro Expression<each Input, Output>((repeat each Input) -> Output) -> Expression<repeat each Input, Output>](expression(_:).md)
- [macro Predicate<each Input>((repeat each Input) -> Bool) -> Predicate<repeat each Input>](predicate(_:).md)
### Type Aliases
- [typealias uuid_string_t](uuid_string_t.md)
- [typealias uuid_t](uuid_t.md)

## See Also

- [Foundation Enumerations](foundation-enumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/foundation-data-types)*