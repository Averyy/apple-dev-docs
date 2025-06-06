# CKToolDatabaseModule

**Framework**: CKTool JS  
**Kind**: class

The imported package that provides access to CloudKit containers and databases.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
interface CKToolDatabaseModule
```

#### Overview

This is the import of all exported content from the `@apple/cktool.database` package.

To access members of `CKToolDatabaseModule` import the `@apple/cktool.database` package the following way:

```javascript
import * as CKToolDatabaseModule from "@apple/cktool.database";
// Example usage
const result = CKToolDatabaseModule.toByte(123);
```

Alternatively, you can import the package symbols directly:

```javascript
import { toByte } from "@apple/cktool.database";
// Example usage
const result = toByte(123);
```

Importing package symbols this way supports tree-shaking.

## Topics

### Instance Methods
- [createUuid](cktooldatabasemodule/createuuid.md)
  Creates a new `Uuid`.
- [toBase64String](cktooldatabasemodule/tobase64string.md)
  Converts a regular string to a `Base64String`.
- [toByte](cktooldatabasemodule/tobyte.md)
  Converts a numeric value to a `Byte`.
- [toByteArray](cktooldatabasemodule/tobytearray.md)
  Converts a numeric array to a `ByteArray`.
- [toDouble](cktooldatabasemodule/todouble.md)
  Converts a number or numeric string to a `Double`.
- [toFloat](cktooldatabasemodule/tofloat.md)
  Converts a number or numeric string to a `Float`.
- [toInt32](cktooldatabasemodule/toint32.md)
  Converts a number to an `Int32`.
- [toInt64](cktooldatabasemodule/toint64.md)
  Converts a number or numeric string to a `Int64`.
- [toNumber](cktooldatabasemodule/tonumber.md)
  Converts a supported numeric type to a JavaScript number.
- [toUuid](cktooldatabasemodule/touuid.md)
  Converts a string to a `Uuid`.

## See Also

- [PromisesApi](promisesapi.md)
  A class that exposes promise-based functions for interacting with the API.
- [CancellablePromise](cancellablepromise.md)
  A promise that has a function to cancel its operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cktooldatabasemodule)*