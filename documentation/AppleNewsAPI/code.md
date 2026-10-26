# Code

**Framework**: AppleNewsAPI  
**Kind**: typealias  
**Role**: Type

See the error codes the Apple News API returned.

**Availability**:
- Apple News API 1.0+

## Declaration

```
string Code
```

## Possible Values

- `API_KEY_NOT_FOUND`: The API key specified in the `Authorization` header does not exist.
- `ARTICLE_TERRITORY_NOT_ALLOWED`: A country code for publishing or updating the article is not supported by your channel.
- `DOES_NOT_EXIST`: The section you specified does not exist.

  Key path: `data.links.sections.#`.
- `DUPLICATE_AUTH_ELEMENT`: Two `Authorization` elements with the same scheme were supplied.
- `FORBIDDEN`: You tried to access a resource that your API key does not have permission to access.

  Key path: None.
- `INCORRECT_HOST`: The section URL has the wrong hostname or port.

  Key path: `data.links.sections.#`.
- `INVALID`:

  - The `pageToken` parameter is not a valid token returned in a `next` link or `nextPageToken` field. Key path: `pageToken`
  - The `sortDir` parameter is not `ASC` or `DESC`. Key path: `sortDir`
  - The `fromDate` parameter is not in ISO 8601 date format. Key path: `fromDate`
  - The `toDate` parameter is not in ISO 8601 date format. Key path: `toDate`
  - The `pageSize` parameter is not an integer in the range 1 to 100, inclusive. Key path: `pageSize.`
  - The specified article ID is not a valid `UUID.` Key path: `data.promotedArticle`
- `INVALID_AUTH_FORMAT`: The `Authorization` header parameters were not parseable as key-value pairs separated by semicolons.
- `INVALID_AUTH_SCHEME`: The first part of the `Authorization` header was not “`HHMAC`”.
- `INCORRECT_ENCODING`: The body of the request is not encoded with the encoding specified in `Content-Encoding`.

  Key path: None.
- `INVALID_JSON`: The JSON specified in the request cannot be parsed as JSON.

  Key path: None.
- `INVALID_RESOURCE_ID`: The section URL has a section ID that is not a valid UUID.

  Key path: `data.links.sections.#`.
- `INVALID_RESOURCE_TYPE`: The path in the section URL does not start with `/sections/`.

  Key path: `data.links.sections.#`.
- `INVALID_SCHEME`: The section URL must have the `https` scheme.

  Key path: `data.links.sections.#`.
- `INVALID_TYPE`: The value specified for `field_name` is not of the correct type for that field.

  Key path: `{field_name}`.
- `INVALID_URL`: The section URL you specified is not a valid URL.

  Key path: `data.links.sections.#`.
- `METHOD_NOT_ALLOWED`: The HTTP method you specified is not valid for this URL.

  Key path: None.
- `DATE_NOT_RECENT`: The date field specified in the `Authorization` header was not within 5 minutes of the server’s time.
- `MISSING`: A required field is missing. The key path indicates the field that was not supplied in the request.

  Key path: *
- `MISSING_API_KEY_ID`: The key field was empty in the `Authorization` header.
- `MISSING_RESOURCE_ID`: The section URL is missing the `section_id` UUID.

  Key path: `data.links.sections.#`.
- `MISSING_SIGNATURE`: The signature field was empty in the `Authorization` header.
- `MISSING_DATE`: The date field was empty in the `Authorization` header.
- `MIME_PART_INVALID_SIZE`: The `size` parameter is not an integer greater than or equal to zero.
- `NOT_ACCEPTABLE`: The `Accept` header, if specified, must allow `application/json`.

  Key path: None.
- `NOT_FOUND`:

  - The endpoint you tried to access does not exist. Key path: None.
  - The resource you tried to access does not exist. Key path: `{resource_id}`.
- `NOT_ALLOWED`:

  - The section you specified does not belong to the given channel. Key path: `data.links.sections.#`.
  - Once an article has been published with `isPreview` set to `false`, the setting cannot be changed to `true.` Key path: `data.isPreview`.
- `UNSUPPORTED_MEDIA_TYPE`: The `Content-Type` value specified is not supported by the specified endpoint.

  Key path: None.
- `UNSUPPORTED_ENCODING`: The encoding specified in `Content-Type` or `Content-Transfer-Encoding` is not supported.

  Key path: None.
- `UNAUTHORIZED`: The `Authorization` header was not set.
- `INVALID_API_KEY_FORMAT`: The `key` field in the `Authorization` header was not a UUID.
- `DUPLICATE_ARTICLE_FOUND`: An article with the same title was published to the same channel within the last 24 hours.
- `DUPLICATE_AUTH_PARAMETER`: A parameter was supplied twice in the `Authorization` header.
- `INVALID_DATE_FORMAT`: The date field specified in the `Authorization` header was not in ISO 8601 format.
- `INVALID_DOCUMENT`: The JSON in the Apple News Format document (`article.json`) is invalid. Test with News Preview first.

  Key path: None.
- `INVALID_MIME_MULTIPART`: The request body cannot be parsed as valid MIME-multipart.

  Key path: None.
- `MIME_PART_TOO_LARGE`: The specified MIME part is larger than 20 MB. Key path: `{mime_part_name}`
- `MIME_PART_TOO_SLOW`: The MIME part took too long to load from the request body. Key path: `{mime_part_name}`
- `MIME_PART_INCORRECT_SIZE`: The `size` specified does not match the actual size of the MIME part.
- `FAILED_TO_PARSE_IMAGE`: The image is either a bad image or has an invalid format.
- `ONLY_PREVIEW_ALLOWED`: This channel is currently only allowed to publish preview articles, but `isPreview` is `false`.

  Key path: None.
- `PUBLISHING_NOT_ALLOWED`: This channel is currently not allowed to publish articles.

  Key path: None.
- `INVALID_ARTICLE_TERRITORY`: A country code for publishing or updating the article is invalid.
- `REQUEST_BODY_TOO_LARGE`: The request body is too large. The maximum size allowed is 500 MB.
- `TOO_MANY_PREVIEW_ARTICLES`: More than 500 articles are not allowed in `isPreview` mode.
- `VIDEO_URL_NOT_ALLOWED`: Your channel does not support `videoURL` in articles.
- `WRONG_REVISION`: The revision specified does not match the current revision, most likely because the article has been updated by another call.

  Key path: `data.revision`.
- `WRONG_SIGNATURE`: The `signature` field given by the client did not match the signature computed by the server.

## See Also

### Errors
- [About Apple News API Error Messages](../AppleNews/about-apple-news-api-error-messages.md)
  Understand the error message format for the Apple News API.
- [object Warning](./warning.md)
  See the properties of a warning the Apple News API returned.
- [object Error](./error.md)
  See the properties of an error the Apple News API returned.
- [type Status](./status.md)
  See the HTTP status codes the Apple News API returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsapi/code)*