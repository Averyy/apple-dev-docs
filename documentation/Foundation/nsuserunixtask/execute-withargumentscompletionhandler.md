# execute(withArguments:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Execute the unix script with the specified arguments.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func execute(withArguments arguments: [String]?) async throws
```

#### Discussion

This method should be invoked no more than once for a given instance of the class.

If the script completed normally, the completion handler’s `error` parameter will be `nil`.

## Parameters

- `arguments`: An array of   objects containing the script arguments. The arguments do not undergo shell expansion, so you do not need to do special quoting, and shell variables are not resolved.
- `handler`: The completion handler Block that returns the result. See  .

## See Also

- [var standardOutput: FileHandle?](nsuserunixtask/standardoutput.md)
  The standard output stream.
- [var standardError: FileHandle?](nsuserunixtask/standarderror.md)
  The standard error stream.
- [init(url: URL) throws](nsuserscripttask/init(url:).md)
  Return a user script task instance given a URL for a script file.
- [var standardInput: FileHandle?](nsuserunixtask/standardinput.md)
  The standard input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserunixtask/execute(witharguments:completionhandler:))*