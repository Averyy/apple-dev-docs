# pasteboard:provideDataForType:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Implemented by an owner object to provide promised data.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```objc
- (void) pasteboard:(NSPasteboard *) sender provideDataForType:(NSPasteboardType) type;
```

## Discussion

The receiver should have been previously declared in a [`declareTypes(_:owner:)`](../../AppKit/nspasteboard/declaretypes%28_,owner%29.md) message.

The requested data should be written to `sender` using the [`setData(_:forType:)`](../../AppKit/nspasteboard/setdata%28_,fortype%29.md), [`setPropertyList(_:forType:)`](../../AppKit/nspasteboard/setpropertylist%28_,fortype%29.md), or [`setString(_:forType:)`](../../AppKit/nspasteboard/setstring%28_,fortype%29.md) method. The [`pasteboard:provideDataForType:`](./pasteboard_providedatafortype_.md) messages may also be sent to the owner when the application is shut down through an application’s [`terminate(_:)`](../../AppKit/nsapplication/terminate%28_%29.md) method. This is the method that is invoked in response to a Quit command. Thus the user can copy something to the pasteboard, quit the application, and still paste the data that was copied. A [`pasteboard:provideDataForType:`](./pasteboard_providedatafortype_.md) message is sent only if the specified type of data has not already been supplied to the pasteboard. Instead of writing all data types when the cut or copy operation is done, an application can choose to implement this method to provide the data for certain types only when they are requested.

If an application writes data to the pasteboard in the richest, and therefore most preferred, type at the time of a cut or copy operation, its [`pasteboard:provideDataForType:`](./pasteboard_providedatafortype_.md) method can simply read that data from the pasteboard, convert it to the requested type, and write it back to the pasteboard as the new type.

## Parameters

- `sender`: The pasteboard that requires the specified data for a paste operation.
- `type`: The type of data the owner object must provide.

## See Also

### Related Documentation
- [Pasteboard Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PasteboardGuide106/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008099)


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/pasteboard:providedatafortype:)*