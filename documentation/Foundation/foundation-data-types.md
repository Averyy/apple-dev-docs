# Foundation Data Types

**Framework**: Foundation  
**Role**: API Collection

This document describes the data types and constants found in the Foundation framework.

## Topics

### Classes
- [class NSKeyValueObservation](./nskeyvalueobservation.md)
- [class NSKeyValueSharedObservers](./nskeyvaluesharedobservers.md)
  A collection of key-value observations which may be registered with multiple observable objects
- [class NSKeyValueSharedObserversSnapshot](./nskeyvaluesharedobserverssnapshot.md)
  A collection of key-value observations which may be registered with multiple observable objects. Create using `-[NSKeyValueSharedObservers snapshot]`
- [NSConstantString](./nsconstantstring.md)
- [NSLocalizedNumberFormatRule](./nslocalizednumberformatrule.md)
- [NSSimpleCString](./nssimplecstring.md)
### Protocols
- [protocol DiscreteFormatStyle](./discreteformatstyle.md)
  A format style that transforms a continuous input into a discrete output and provides information about its discretization boundaries.
- [protocol NSKeyValueObservingCustomization](./nskeyvalueobservingcustomization.md)
  Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys
### Structures
- [struct AsyncCharacterSequence](./asynccharactersequence.md)
  An asynchronous sequence of characters.
- [struct AsyncLineSequence](./asynclinesequence.md)
  An asynchronous sequence of lines of text.
- [struct AsyncUnicodeScalarSequence](./asyncunicodescalarsequence.md)
  An asychronous sequence of Unicode scalar values.
- [struct Expression](./expression.md)
- [struct NSAttributedStringFormattingContextKey](./nsattributedstringformattingcontextkey.md)
  A type that represents a key in the formatting context dictionary.
- [struct NSKeyValueChangeKey](./nskeyvaluechangekey.md)
  The keys that can appear in the change dictionary.
- [struct NSKeyValueObservedChange](./nskeyvalueobservedchange.md)
- [struct NSKeyValueOperator](./nskeyvalueoperator.md)
  These constants define the available array operators. See [Using Collection Operators](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/CollectionOperators.html) for more information.
- [struct PresentationIntent](./presentationintent.md)
  A type that defines presentation intent for blocks of characters like paragraphs, lists, block quotes, and tables.
### Variables
- [let NSOperationNotSupportedForKeyException: String](./nsoperationnotsupportedforkeyexception.md)
- [let NSURLSessionUploadTaskResumeData: String](./nsurlsessionuploadtaskresumedata.md)
  Key in the userInfo dictionary of an NSError received during a failed upload.
- [var kCFStringEncodingASCII: CFStringEncoding](./kcfstringencodingascii.md)
### Macros
- [macro Expression<each Input, Output>((repeat each Input) -> Output) -> Expression<repeat each Input, Output>](./expression%28_%29.md)
- [macro Predicate<each Input>((repeat each Input) -> Bool) -> Predicate<repeat each Input>](./predicate%28_%29.md)
- [ABS](./abs.md)
- [FOUNDATION_EXPORT](./foundation_export.md)
- [FOUNDATION_EXTERN](./foundation_extern.md)
- [FOUNDATION_EXTERN_INLINE](./foundation_extern_inline.md)
- [FOUNDATION_IMPORT](./foundation_import.md)
- [FOUNDATION_STATIC_INLINE](./foundation_static_inline.md)
- [FOUNDATION_SWIFT_SDK_EPOCH_AT_LEAST](./foundation_swift_sdk_epoch_at_least.md)
- [MAX](./max.md)
- [MIN](./min.md)
- [NS_ASSUME_NONNULL_BEGIN](./ns_assume_nonnull_begin.md)
- [NS_ASSUME_NONNULL_END](./ns_assume_nonnull_end.md)
- [NS_AUTOMATED_REFCOUNT_UNAVAILABLE](./ns_automated_refcount_unavailable.md)
- [NS_AUTOMATED_REFCOUNT_WEAK_UNAVAILABLE](./ns_automated_refcount_weak_unavailable.md)
- [NS_AVAILABLE](./ns_available.md)
- [NS_AVAILABLE_IOS](./ns_available_ios.md)
- [NS_AVAILABLE_IPHONE](./ns_available_iphone.md)
- [NS_AVAILABLE_MAC](./ns_available_mac.md)
- [NS_BLOCKS_AVAILABLE](./ns_blocks_available.md)
- [NS_CALENDAR_DEPRECATED](./ns_calendar_deprecated.md)
- [NS_CALENDAR_DEPRECATED_MAC](./ns_calendar_deprecated_mac.md)
- [NS_CALENDAR_ENUM_DEPRECATED](./ns_calendar_enum_deprecated.md)
- [NS_CLASS_AVAILABLE](./ns_class_available.md)
- [NS_CLASS_AVAILABLE_IOS](./ns_class_available_ios.md)
- [NS_CLASS_AVAILABLE_MAC](./ns_class_available_mac.md)
- [NS_CLASS_DEPRECATED](./ns_class_deprecated.md)
- [NS_CLASS_DEPRECATED_IOS](./ns_class_deprecated_ios.md)
- [NS_CLASS_DEPRECATED_MAC](./ns_class_deprecated_mac.md)
- [NS_CLOSED_ENUM](./ns_closed_enum.md)
- [NS_DEPRECATED](./ns_deprecated.md)
- [NS_DEPRECATED_IOS](./ns_deprecated_ios.md)
- [NS_DEPRECATED_IPHONE](./ns_deprecated_iphone.md)
- [NS_DEPRECATED_MAC](./ns_deprecated_mac.md)
- [NS_DEPRECATED_WITH_REPLACEMENT_MAC](./ns_deprecated_with_replacement_mac.md)
- [NS_ENUM](./ns_enum.md)
- [NS_ENUM_AVAILABLE](./ns_enum_available.md)
- [NS_ENUM_AVAILABLE_IOS](./ns_enum_available_ios.md)
- [NS_ENUM_AVAILABLE_MAC](./ns_enum_available_mac.md)
- [NS_ENUM_DEPRECATED](./ns_enum_deprecated.md)
- [NS_ENUM_DEPRECATED_IOS](./ns_enum_deprecated_ios.md)
- [NS_ENUM_DEPRECATED_MAC](./ns_enum_deprecated_mac.md)
- [NS_ERROR_ENUM](./ns_error_enum.md)
- [NS_EXTENSIBLE_STRING_ENUM](./ns_extensible_string_enum.md)
- [NS_EXTENSION_UNAVAILABLE](./ns_extension_unavailable.md)
- [NS_EXTENSION_UNAVAILABLE_IOS](./ns_extension_unavailable_ios.md)
- [NS_EXTENSION_UNAVAILABLE_MAC](./ns_extension_unavailable_mac.md)
- [NS_FALLTHROUGH](./ns_fallthrough.md)
- [NS_FORMAT_ARGUMENT](./ns_format_argument.md)
- [NS_FORMAT_FUNCTION](./ns_format_function.md)
- [NS_HEADER_AUDIT_BEGIN](./ns_header_audit_begin.md)
- [NS_HEADER_AUDIT_END](./ns_header_audit_end.md)
- [NS_INLINE](./ns_inline.md)
- [NS_NO_TAIL_CALL](./ns_no_tail_call.md)
- [NS_NOESCAPE](./ns_noescape.md)
- [NS_NONATOMIC_IOSONLY](./ns_nonatomic_iosonly.md)
- [NS_NONATOMIC_IPHONEONLY](./ns_nonatomic_iphoneonly.md)
- [NS_OPTIONS](./ns_options.md)
- [NS_PROTOCOL_REQUIRES_EXPLICIT_IMPLEMENTATION](./ns_protocol_requires_explicit_implementation.md)
- [NS_REFINED_FOR_SWIFT](./ns_refined_for_swift.md)
- [NS_REFINED_FOR_SWIFT_ASYNC](./ns_refined_for_swift_async.md)
- [NS_RELEASES_ARGUMENT](./ns_releases_argument.md)
- [NS_REPLACES_RECEIVER](./ns_replaces_receiver.md)
- [NS_REQUIRES_NIL_TERMINATION](./ns_requires_nil_termination.md)
- [NS_REQUIRES_PROPERTY_DEFINITIONS](./ns_requires_property_definitions.md)
- [NS_REQUIRES_SUPER](./ns_requires_super.md)
- [NS_RETURNS_INNER_POINTER](./ns_returns_inner_pointer.md)
- [NS_RETURNS_NOT_RETAINED](./ns_returns_not_retained.md)
- [NS_RETURNS_RETAINED](./ns_returns_retained.md)
- [NS_ROOT_CLASS](./ns_root_class.md)
- [NS_STRING_ENUM](./ns_string_enum.md)
- [NS_SWIFT_ASYNC](./ns_swift_async.md)
- [NS_SWIFT_ASYNC_NAME](./ns_swift_async_name.md)
- [NS_SWIFT_ASYNC_NOTHROW](./ns_swift_async_nothrow.md)
- [NS_SWIFT_ASYNC_THROWS_ON_FALSE](./ns_swift_async_throws_on_false.md)
- [NS_SWIFT_ASYNC_THROWS_ON_TRUE](./ns_swift_async_throws_on_true.md)
- [NS_SWIFT_BRIDGED_TYPEDEF](./ns_swift_bridged_typedef.md)
- [NS_SWIFT_DISABLE_ASYNC](./ns_swift_disable_async.md)
- [NS_SWIFT_NAME](./ns_swift_name.md)
- [NS_SWIFT_NONISOLATED](./ns_swift_nonisolated.md)
- [NS_SWIFT_NONSENDABLE](./ns_swift_nonsendable.md)
- [NS_SWIFT_NOTHROW](./ns_swift_nothrow.md)
- [NS_SWIFT_SENDABLE](./ns_swift_sendable.md)
- [NS_SWIFT_SENDING](./ns_swift_sending.md)
- [NS_SWIFT_UI_ACTOR](./ns_swift_ui_actor.md)
- [NS_SWIFT_UNAVAILABLE](./ns_swift_unavailable.md)
- [NS_SWIFT_UNAVAILABLE_FROM_ASYNC](./ns_swift_unavailable_from_async.md)
- [NS_TYPED_ENUM](./ns_typed_enum.md)
- [NS_TYPED_EXTENSIBLE_ENUM](./ns_typed_extensible_enum.md)
- [NS_UNAVAILABLE](./ns_unavailable.md)
- [NS_UNICHAR_IS_EIGHT_BIT](./ns_unichar_is_eight_bit.md)
- [NS_VALID_UNTIL_END_OF_SCOPE](./ns_valid_until_end_of_scope.md)
  Marks local variables of type `id` or pointer-to-ObjC-object-type so that values stored into those local variable are not aggressively released by the compiler during optimization. Instead, the values are held until either the variable is assigned to again, or the end of the scope of the local variable (such as in a compound statement or a method definition).
- [NS_WARN_UNUSED_RESULT](./ns_warn_unused_result.md)
- [NSEDGEINSETS_DEFINED](./nsedgeinsets_defined.md)
- [NSGEOMETRY_TYPES_SAME_AS_CGGEOMETRY_TYPES](./nsgeometry_types_same_as_cggeometry_types.md)
- [NSLocalizedAttributedString](./nslocalizedattributedstring.md)
- [NSLocalizedAttributedStringFromTable](./nslocalizedattributedstringfromtable.md)
- [NSLocalizedAttributedStringFromTableInBundle](./nslocalizedattributedstringfromtableinbundle.md)
- [NSLocalizedAttributedStringWithDefaultValue](./nslocalizedattributedstringwithdefaultvalue.md)
- [NSObjectAutoreleasedEvent](./nsobjectautoreleasedevent.md)
- [NSObjectExtraRefDecrementedEvent](./nsobjectextrarefdecrementedevent.md)
- [NSObjectExtraRefIncrementedEvent](./nsobjectextrarefincrementedevent.md)
- [NSObjectInternalRefDecrementedEvent](./nsobjectinternalrefdecrementedevent.md)
- [NSObjectInternalRefIncrementedEvent](./nsobjectinternalrefincrementedevent.md)
- [NSOperationQualityOfService](./nsoperationqualityofservice.md)
- [NSOperationQualityOfServiceBackground](./nsoperationqualityofservicebackground.md)
- [NSOperationQualityOfServiceUserInitiated](./nsoperationqualityofserviceuserinitiated.md)
- [NSOperationQualityOfServiceUserInteractive](./nsoperationqualityofserviceuserinteractive.md)
- [NSOperationQualityOfServiceUtility](./nsoperationqualityofserviceutility.md)
- [NSURLSESSION_AVAILABLE](./nsurlsession_available.md)
- [NS_SWIFT_NONISOLATED_UNSAFE](./ns_swift_nonisolated_unsafe.md)
### Type Aliases
- [typealias uuid_string_t](./uuid_string_t.md)
- [typealias uuid_t](./uuid_t.md)

## See Also

### Reference
- [Foundation Enumerations](./foundation-enumerations.md)
- [Foundation Constants](./foundation-constants.md)
  This document defines constants in the Foundation framework that are not associated with a particular class.
- [Foundation Functions](./foundation-functions.md)
  This document describes the functions and function-like macros defined in the Foundation Framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/foundation-data-types)*