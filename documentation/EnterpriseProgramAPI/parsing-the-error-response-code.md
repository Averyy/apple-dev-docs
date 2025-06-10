# Parsing the Error Response Code

**Framework**: Enterprise Program API

Interpret the error details to troubleshoot API requests and perform programmatic error handling.

#### Overview

When your API request results in an error, you receive an [`ErrorResponse`](errorresponse.md) that contains an array of errors. The `code` property of the [`ErrorResponse`](errorresponse.md) helps you identify which part of your request may contain an error.

The error data (`ErrorResponse.Data`) fully describes an error through its properties, including `status`, `id`, `title`, `code`, and others. However, for programmatic error handling, use only the `code` property.

##### Parse the Error Code

The `code` property is a stable, machine-readable value indicating the exact type of error. The `code` is hierarchical, with dots separating the information about the error from general to specific. The more information the system has about the error, the more levels the error code includes. For example, the error code `ENTITY_ERROR.ATTRIBUTE.INVALID` has three levels, and tells you:

1. `ENTITY_ERROR`: On the most general level, a problem occurred with the request entity.
2. `ATTRIBUTE`: On a more specific level, a problem occurred with one of the resource attributes in the entity.
3. `INVALID`: On a very specific level, the resource attribute contains an invalid value.

In many cases, the most general level of information provides all you need to know about the error. In that case, a prefix match on `ENTITY_ERROR` can detect and respond to any entity error. If you need to handle invalid attributes specifically, you can inspect the full code value.

> 💡 **Tip**:  Examine the error code using prefix matching rather than exact string comparison. Exact string comparison may not work if the error code includes additional levels of detail.

##### Relate Error Codes to the Parts of the Request

You can analyze the parts of your request in order to trace the correlating error information. Requests consist of a method, path, and parameters or a request entity, as shown in the `GET` request annotated below.

![An annotated GET request.](https://docs-assets.developer.apple.com/published/2202ca8fd35433677f793fc5d2e946f2/media-3040420%402x.png)

Likewise, the parts of a `POST` request are annotated below.

![An annotated POST request.](https://docs-assets.developer.apple.com/published/1be9cf8b321a4afd2daddc907a772786/media-3074413%402x.png)

If there’s an error in a request, the response returns an HTTP status code in the 400 range. The `code` parameter of the [`ErrorResponse`](errorresponse.md) helps you identify which part of your request may contain an error: the method, path, parameter, or entity.

##### Identify Errors with the Method

Responses that indicate the request’s  contains an error include:

- `405` `METHOD_NOT_ALLOWED`: The method and path combination is not valid in the API. For example, `PATCH https://api.enterprise.developer.apple.com/v1/certificates` is not valid because `PATCH` is not supported for the `certificates` resource.
- `403` `FORBIDDEN_ERROR`: The method and path combination is valid, but not allowed due to business rules; for example, because the caller’s role permissions don’t allow access.

##### Identify Errors with the Path

Responses that indicate the request’s  contains an error include:

- `404 PATH_ERROR`: The path is not valid. For example, `GET https://api.enterprise.developer.apple.com/v1/bananas` is not a valid path in this API.
- `404 NOT_FOUND`: The resource does not exist. For example, `GET https://api.enterprise.developer.apple.com/v1/apps/9999999999` is requesting an app with an ID that does not exist.

##### Identify Errors with the Parameters

Responses that indicate one of the request’s  contain an error include:

- `400 PARAMETER_ERROR.ILLEGAL`: The parameter is not valid in this API. For example, in `GET https://api.enterprise.developer.apple.com/v1/users?foo=1`, “`foo`” is not a valid parameter.
- `400` `PARAMETER_ERROR.INVALID`: The parameter is allowed but has an invalid `value` or `type`.
- `400` `PARAMETER_ERROR.REQUIRED`: A required parameter is missing.

##### Identify Errors with the Request Entity

Responses that indicate the request’s  contains an error include:

- `400 ENTITY_INVALID`: The request entity is the wrong type and is not valid JSON.
- `409 ENTITY_ERROR`: The request entity is valid and in the right format, but the data in it is unacceptable; for example, it contains an invalid email address, or a duplicate locale.
- `422 ENTITY_UNPROCESSABLE`:` `The request entity is JSON but it is not the right format; for example, it contains misspelled keys for “`data`” or “`attributes`”.

## See Also

- [About the HTTP Status Code](about-the-http-status-code.md)
  Learn how the status code helps you determine if an Enterprise Program  API request succeeded or why it failed.
- [Pinpointing the Location of Errors](pinpointing-the-location-of-errors.md)
  Locate the specific source of the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/parsing-the-error-response-code)*