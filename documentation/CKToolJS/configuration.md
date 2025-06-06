# Configuration

**Framework**: CKTool JS  
**Kind**: class

An object you use to hold options for communicating with the API server.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
interface Configuration
```

#### Overview

A `createConfiguration` function from one of the `@apple/cktool.target.browser` or `@apple/cktool.target.nodejs` packages creates an instance of this class appropriate for your target platform.

Note: You shouldn’t create instances of this class directly.

## Topics

### Initializers
- [Configuration](configuration/configuration.md)
  Internal use only.
### Instance Properties
- [jsonParse](configuration/jsonparse.md)
  A function that a response parser uses to interpret JSON from the API server.
- [jsonStringify](configuration/jsonstringify.md)
  A function that a request function uses to prepare JSON to send to the API server.
- [serverUrl](configuration/serverurl.md)
  The URL of the API server.

## See Also

- [CKToolNodeJsModule](cktoolnodejsmodule.md)
  The imported package that supports using the client library within a Node.js environment.
- [CKToolBrowserModule](cktoolbrowsermodule.md)
  The imported package that supports using the client library within a web browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/configuration)*