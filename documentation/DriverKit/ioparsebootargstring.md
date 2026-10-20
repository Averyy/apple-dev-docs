# IOParseBootArgString

**Framework**: DriverKit  
**Kind**: func  
**Role**: Function

Parses any boot arguments in the macOS kernel boot-args.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
bool IOParseBootArgString(const char *arg_string, char *arg_ptr, int strlen);
```

#### Return Value

True if the argument was found and parsed successfully to arg_ptr.

#### Discussion

If the named argument is present in the kernel boot-args, return its value as a c-string.

## Parameters

- `arg_string`: C-string name of the argument.
- `arg_ptr`: Pointer to char array to received parsed value.
- `strlen`: Size in bytes of the char array pointed to by arg_ptr.

## See Also

### Boot Support
- [IOParseBootArgNumber](./ioparsebootargnumber.md)
  Parses any boot arguments in the macOS kernel boot-args.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioparsebootargstring)*