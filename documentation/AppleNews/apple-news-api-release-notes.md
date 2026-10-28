# Apple News API Release Notes

**Framework**: Apple News  
**Role**: Article

Learn about new features that require iOS 26, iPadOS 26, and macOS 26.

## Overview

These features were added in the latest Apple News API release:

- The [`Create an Article`](../AppleNewsAPI/post-channels-_channelid_-articles.md) endpoint throws a 400 error if you attempt to publish an article bundle exceeding 450 MB.
- The [`Update an Article`](../AppleNewsAPI/post-articles-_articleid_.md) endpoint throws a 400 error if you attempt to update an article bundle exceeding 450 MB.

These features were added in a previous Apple News API release:

- The [`Create an Article`](../AppleNewsAPI/post-channels-_channelid_-articles.md) endpoint throws a 400 error if you attempt to publish an article with a publication date before 1970, and a warning if the publication date is before 2015.
- The [`Update an Article`](../AppleNewsAPI/post-articles-_articleid_.md) endpoint throws a 400 error if you attempt to update an article with a publication date before 1970, and a warning if the publication date is before 2015.

This field is no longer supported in Apple News API:

- `accessoryText` is deprecated in [`Create Article Metadata Fields`](../AppleNewsAPI/create-article-metadata-fields.md) and [`Update Article Metadata Fields`](../AppleNewsAPI/update-article-metadata-fields.md). Use the `authors` property in the Apple News Format [`Metadata`](../AppleNewsFormat/metadata.md) object instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/apple-news-api-release-notes)*