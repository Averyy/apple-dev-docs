# PromisesApi

**Framework**: CKTool JS  
**Kind**: init

Creates a `PromisesApi` object.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
new defaultOptions(
	PromisesApiOptions defaultOptions
);
```

#### Discussion

You create an instance of `PromisesApi` in order to interact with the API. Methods on this class return promises that complete with a response object.

```javascript
import { PromisesApi } from "@apple/cktool.database";
import { createConfiguration } from "@apple/cktool.target.nodejs";
 
const api = new PromisesApi({
  configuration: createConfiguration(),
  security: { “ManagementTokenAuth”: “YOUR_MANAGEMENT_TOKEN” }
});
```

The `defaultOptions` dictionary has the following properties:

```javascript
dictionary PromisesApiOptions {
  Configuration: configuration;
  Security?: security;
}
```

- `configuration`: The `Configuration` instance created with `createConfiguration`.
- `security`: The dictionary of your authorization tokens.

## Parameters

- `defaultOptions`: A dictionary as described in the Discussion section.

## See Also

- [PromisesApiOptions](promisesapioptions.md)
  A dictionary of options for promises API classes.
- [Security](security.md)
  A dictionary of your authorization tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi/promisesapi)*