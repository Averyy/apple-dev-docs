# CFShow(_:)

**Framework**: Core Foundation  
**Kind**: func

Prints a description of a Core Foundation object to stderr.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFShow(_ obj: CFTypeRef!)
```

#### Discussion

The output is printed to the standard I/O standard error (stderr).

This function is useful as a debugging aid for Core Foundation objects. Because these objects are based on opaque types, it is difficult to examine their contents directly. However, the opaque types implement `description` function callbacks that return descriptions of their objects. This function invokes these callbacks.

##### Special Considerations

You can use `CFShow` in one of two general ways. If your debugger supports function calls (such as `gdb` does), call `CFShow` in the debugger:

```objc
(gdb) call (void) CFShow(string)
Hello World
```

You can also incorporate calls to `CFShow` in a test version of your code to print out “snapshots” of Core Foundation objects to the console.

## Parameters

- `obj`: A Core Foundation object derived from CFType. If   is not a Core Foundation object, an assertion is raised.

## See Also

- [func CFCopyDescription(CFTypeRef!) -> CFString!](cfcopydescription(_:).md)
  Returns a textual description of a Core Foundation object.
- [func CFCopyTypeIDDescription(CFTypeID) -> CFString!](cfcopytypeiddescription(_:).md)
  Returns a textual description of a Core Foundation type, as identified by its type ID, which can be used when debugging.
- [func CFGetTypeID(CFTypeRef!) -> CFTypeID](cfgettypeid(_:).md)
  Returns the unique identifier of an opaque type to which a Core Foundation object belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfshow(_:))*