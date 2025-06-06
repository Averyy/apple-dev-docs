# IOParseBootArgNumber

**Framework**: DriverKit  
**Kind**: func

Parses any boot arguments in the macOS kernel boot-args.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool IOParseBootArgNumber(const char * arg_string, void * arg_ptr, int max_len);
```

#### Return Value

True if the argument was found and parsed successfully to arg_ptr.

#### Discussion

If the named argument is present in the kernel boot-args, return its value as an integer.

## Parameters

- `arg_string`: C-string name of the argument.
- `arg_ptr`: Pointer to variable to received parsed value.
- `max_len`: Size in bytes of the argument pointed to by arg_ptr.

## See Also

- [IOParseBootArgString](ioparsebootargstring.md)
  Parses any boot arguments in the macOS kernel boot-args.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioparsebootargnumber)*