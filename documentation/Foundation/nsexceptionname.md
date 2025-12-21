# NSExceptionName

**Framework**: Foundation  
**Kind**: struct

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
struct NSExceptionName
```

## Topics

### Type Properties
- [static let characterConversionException: NSExceptionName](nsexceptionname/characterconversionexception.md)
  `NSString` raises an `NSCharacterConversionException` if a string cannot be represented in a file-system or string encoding.
- [static let decimalNumberDivideByZeroException: NSExceptionName](nsexceptionname/decimalnumberdividebyzeroexception.md)
  The exception raised on divide by zero.
- [static let decimalNumberExactnessException: NSExceptionName](nsexceptionname/decimalnumberexactnessexception.md)
  The exception raised if there is an exactness error.
- [static let decimalNumberOverflowException: NSExceptionName](nsexceptionname/decimalnumberoverflowexception.md)
  The exception raised on overflow.
- [static let decimalNumberUnderflowException: NSExceptionName](nsexceptionname/decimalnumberunderflowexception.md)
  The exception raised on underflow.
- [static let destinationInvalidException: NSExceptionName](nsexceptionname/destinationinvalidexception.md)
  Name of an exception that occurs when an internal assertion fails and implies an unexpected condition within the distributed objects.
- [static let fileHandleOperationException: NSExceptionName](nsexceptionname/filehandleoperationexception.md)
  Raised by `NSFileHandle` if attempts to determine file-handle type fail or if attempts to read from a file or channel fail.
- [static let genericException: NSExceptionName](nsexceptionname/genericexception.md)
  A generic name for an exception.
- [static let internalInconsistencyException: NSExceptionName](nsexceptionname/internalinconsistencyexception.md)
  Name of an exception that occurs when an internal assertion fails and implies an unexpected condition within the called code.
- [static let invalidArchiveOperationException: NSExceptionName](nsexceptionname/invalidarchiveoperationexception.md)
  The name of the exception raised by `NSKeyedArchiver` if there is a problem creating an archive.
- [static let invalidArgumentException: NSExceptionName](nsexceptionname/invalidargumentexception.md)
  Name of an exception that occurs when you pass an invalid argument to a method, such as a `nil` pointer where a non-`nil` object is required.
- [static let invalidReceivePortException: NSExceptionName](nsexceptionname/invalidreceiveportexception.md)
  Name of an exception that occurs when the receive port of an `NSConnection` has become invalid.
- [static let invalidSendPortException: NSExceptionName](nsexceptionname/invalidsendportexception.md)
  Name of an exception that occurs when the send port of an `NSConnection` has become invalid.
- [static let invalidUnarchiveOperationException: NSExceptionName](nsexceptionname/invalidunarchiveoperationexception.md)
  The name of the exception raised by `NSKeyedArchiver` if there is a problem extracting an archive.
- [static let invocationOperationCancelledException: NSExceptionName](nsexceptionname/invocationoperationcancelledexception.md)
  The name of the exception raised if the [`result`](nsinvocationoperation/result.md) method is called after the operation was cancelled.
- [static let invocationOperationVoidResultException: NSExceptionName](nsexceptionname/invocationoperationvoidresultexception.md)
  The name of the exception raised if the [`result`](nsinvocationoperation/result.md) method is called for an invocation method with a `void` return type.
- [static let mallocException: NSExceptionName](nsexceptionname/mallocexception.md)
  Obsolete; not currently used.
- [static let objectInaccessibleException: NSExceptionName](nsexceptionname/objectinaccessibleexception.md)
  Name of an exception that occurs when a remote object is accessed from a thread that should not access it.
- [static let objectNotAvailableException: NSExceptionName](nsexceptionname/objectnotavailableexception.md)
  Name of an exception that occurs when the remote side of the `NSConnection` refused to send the message to the object because the object has never been vended.
- [static let oldStyleException: NSExceptionName](nsexceptionname/oldstyleexception.md)
  No longer used.
- [static let parseErrorException: NSExceptionName](nsexceptionname/parseerrorexception.md)
  `NSString` raises an `NSParseErrorException` if a string cannot be parsed as a property list.
- [static let portReceiveException: NSExceptionName](nsexceptionname/portreceiveexception.md)
  Generic error occurred on receive.
- [static let portSendException: NSExceptionName](nsexceptionname/portsendexception.md)
  Generic error occurred on send.
- [static let portTimeoutException: NSExceptionName](nsexceptionname/porttimeoutexception.md)
  Name of an exception that occurs when a timeout set on a port expires during a send or receive operation.
- [static let rangeException: NSExceptionName](nsexceptionname/rangeexception.md)
  Name of an exception that occurs when attempting to access outside the bounds of some data, such as beyond the end of a string.
- [static let undefinedKeyException: NSExceptionName](nsexceptionname/undefinedkeyexception.md)
  Raised when a key value coding operation fails.
- [static let inconsistentArchiveException: NSExceptionName](nsexceptionname/inconsistentarchiveexception.md)
  The name of an exception raised by [`NSArchiver`](nsarchiver.md) if there are problems initializing or encoding.
- [static let NSPPDIncludeNotFoundException: NSExceptionName](nsexceptionname/nsppdincludenotfoundexception.md)
- [static let NSPPDIncludeStackOverflowException: NSExceptionName](nsexceptionname/nsppdincludestackoverflowexception.md)
- [static let NSPPDIncludeStackUnderflowException: NSExceptionName](nsexceptionname/nsppdincludestackunderflowexception.md)
- [static let NSPPDParseException: NSExceptionName](nsexceptionname/nsppdparseexception.md)
- [static let NSRTFPropertyStackOverflowException: NSExceptionName](nsexceptionname/nsrtfpropertystackoverflowexception.md)
- [static let NSTIFFException: NSExceptionName](nsexceptionname/nstiffexception.md)
- [static let abortModalException: NSExceptionName](nsexceptionname/abortmodalexception.md)
- [static let abortPrintingException: NSExceptionName](nsexceptionname/abortprintingexception.md)
- [static let accessibilityException: NSExceptionName](nsexceptionname/accessibilityexception.md)
- [static let appKitIgnoredException: NSExceptionName](nsexceptionname/appkitignoredexception.md)
- [static let appKitVirtualMemoryException: NSExceptionName](nsexceptionname/appkitvirtualmemoryexception.md)
- [static let badBitmapParametersException: NSExceptionName](nsexceptionname/badbitmapparametersexception.md)
- [static let badComparisonException: NSExceptionName](nsexceptionname/badcomparisonexception.md)
- [static let badRTFColorTableException: NSExceptionName](nsexceptionname/badrtfcolortableexception.md)
- [static let badRTFDirectiveException: NSExceptionName](nsexceptionname/badrtfdirectiveexception.md)
- [static let badRTFFontTableException: NSExceptionName](nsexceptionname/badrtffonttableexception.md)
- [static let badRTFStyleSheetException: NSExceptionName](nsexceptionname/badrtfstylesheetexception.md)
- [static let browserIllegalDelegateException: NSExceptionName](nsexceptionname/browserillegaldelegateexception.md)
- [static let colorListIOException: NSExceptionName](nsexceptionname/colorlistioexception.md)
- [static let colorListNotEditableException: NSExceptionName](nsexceptionname/colorlistnoteditableexception.md)
- [static let draggingException: NSExceptionName](nsexceptionname/draggingexception.md)
- [static let fontUnavailableException: NSExceptionName](nsexceptionname/fontunavailableexception.md)
- [static let illegalSelectorException: NSExceptionName](nsexceptionname/illegalselectorexception.md)
- [static let imageCacheException: NSExceptionName](nsexceptionname/imagecacheexception.md)
- [static let nibLoadingException: NSExceptionName](nsexceptionname/nibloadingexception.md)
- [static let pasteboardCommunicationException: NSExceptionName](nsexceptionname/pasteboardcommunicationexception.md)
- [static let printOperationExistsException: NSExceptionName](nsexceptionname/printoperationexistsexception.md)
  The name of an exception raised when there is already a print operation in process.
- [static let printPackageException: NSExceptionName](nsexceptionname/printpackageexception.md)
- [static let printingCommunicationException: NSExceptionName](nsexceptionname/printingcommunicationexception.md)
- [static let textLineTooLongException: NSExceptionName](nsexceptionname/textlinetoolongexception.md)
  Exception generated if a line is too long in a `NSText` object.
- [static let textNoSelectionException: NSExceptionName](nsexceptionname/textnoselectionexception.md)
- [static let textReadException: NSExceptionName](nsexceptionname/textreadexception.md)
- [static let textWriteException: NSExceptionName](nsexceptionname/textwriteexception.md)
- [static let typedStreamVersionException: NSExceptionName](nsexceptionname/typedstreamversionexception.md)
- [static let windowServerCommunicationException: NSExceptionName](nsexceptionname/windowservercommunicationexception.md)
- [static let wordTablesReadException: NSExceptionName](nsexceptionname/wordtablesreadexception.md)
- [static let wordTablesWriteException: NSExceptionName](nsexceptionname/wordtableswriteexception.md)
- [class let hierarchyInconsistencyException: NSExceptionName](../UIKit/UIViewController/hierarchyInconsistencyException.md)
  Raised if the view controller hierarchy is inconsistent with the view hierarchy.
- [class let invalidInterfaceOrientationException: NSExceptionName](../UIKit/UIApplication/invalidInterfaceOrientationException.md)
  An exception that’s thrown if a view controller or the app returns an invalid set of supported interface orientations.
### Initializers
- [init(String)](nsexceptionname/init(_:).md)
- [init(rawValue: String)](nsexceptionname/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [typealias NSUncaughtExceptionHandler](nsuncaughtexceptionhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexceptionname)*