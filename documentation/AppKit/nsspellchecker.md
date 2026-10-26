# NSSpellChecker

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An interface to the Cocoa spell-checking service.

**Availability**:
- macOS

## Declaration

```swift
class NSSpellChecker
```

```objc
@interface NSSpellChecker : NSObject
```

#### Overview

To handle all its spell checking, an app needs only one instance of [`NSSpellChecker`](./nsspellchecker.md), known as the spell checker. Using the spell checker you manage the Spelling panel, in which the user can specify decisions about words that are suspect. The spell checker also offers the ability to provide word completions to augment the text completion system.

## Topics

### Getting the Spell Checker
- [class var shared: NSSpellChecker](./nsspellchecker/shared.md)
  Returns the NSSpellChecker (one per application).
- [class var sharedSpellCheckerExists: Bool](./nsspellchecker/sharedspellcheckerexists.md)
  Returns whether the application’s NSSpellChecker has already been created.
### Configuring Spell Checkers Languages
- [var availableLanguages: [String]](./nsspellchecker/availablelanguages.md)
  Provides a list of all available languages.
- [var userPreferredLanguages: [String]](./nsspellchecker/userpreferredlanguages.md)
  Provides a subset of the available languages to be used for spell checking.
- [var automaticallyIdentifiesLanguages: Bool](./nsspellchecker/automaticallyidentifieslanguages.md)
  Sets whether the spell checker will automatically identify languages.
- [func language() -> String](./nsspellchecker/language%28%29.md)
  Returns the current language used in spell checking.
- [func setLanguage(String) -> Bool](./nsspellchecker/setlanguage%28_%29.md)
  Returns whether the specified language is in the Spelling pop-up list.
### Managing Panels
- [var spellingPanel: NSPanel](./nsspellchecker/spellingpanel.md)
  Returns the spell checker’s panel.
- [var substitutionsPanel: NSPanel](./nsspellchecker/substitutionspanel.md)
  Returns the substitutions panel.
- [func updateSpellingPanel(withGrammarString: String, detail: [String : Any])](./nsspellchecker/updatespellingpanel%28withgrammarstring,detail%29.md)
  Specifies a grammar-analysis detail to highlight in the Spelling panel.
- [func updatePanels()](./nsspellchecker/updatepanels%28%29.md)
  Updates the available panels to account for user changes.
- [var accessoryView: NSView?](./nsspellchecker/accessoryview.md)
  Makes a view an accessory of the Spelling panel by making it a subview of the panel’s content view.
- [var substitutionsPanelAccessoryViewController: NSViewController?](./nsspellchecker/substitutionspanelaccessoryviewcontroller.md)
  Sets the substitutions panel’s accessory view.
### Checking Strings for Spelling and Grammar
- [func countWords(in: String, language: String?) -> Int](./nsspellchecker/countwords%28in,language%29.md)
  Returns the number of words in the specified string.
- [func checkSpelling(of: String, startingAt: Int) -> NSRange](./nsspellchecker/checkspelling%28of,startingat%29.md)
  Starts the search for a misspelled word in `stringToCheck` starting at `startingOffset` within the string object.
- [func checkSpelling(of: String, startingAt: Int, language: String?, wrap: Bool, inSpellDocumentWithTag: Int, wordCount: UnsafeMutablePointer<Int>?) -> NSRange](./nsspellchecker/checkspelling%28of,startingat,language,wrap,inspelldocumentwithtag,wordcount%29.md)
  Starts the search for a misspelled word in a string starting at specified offset within the string.
- [func checkGrammar(of: String, startingAt: Int, language: String?, wrap: Bool, inSpellDocumentWithTag: Int, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange](./nsspellchecker/checkgrammar%28of,startingat,language,wrap,inspelldocumentwithtag,details%29.md)
  Initiates a grammatical analysis of a given string.
- [func check(String, range: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, orthography: AutoreleasingUnsafeMutablePointer<NSOrthography?>?, wordCount: UnsafeMutablePointer<Int>?) -> [NSTextCheckingResult]](./nsspellchecker/check%28_,range,types,options,inspelldocumentwithtag,orthography,wordcount%29.md)
  Requests unified text checking for the given range of the given string.
- [func requestChecking(of: String, range: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult], NSOrthography, Int) -> Void)?) -> Int](./nsspellchecker/requestchecking%28of,range,types,options,inspelldocumentwithtag,completionhandler%29.md)
  Requests that the string be checked in the background.
- [func guesses(forWordRange: NSRange, in: String, language: String?, inSpellDocumentWithTag: Int) -> [String]?](./nsspellchecker/guesses%28forwordrange,in,language,inspelldocumentwithtag%29.md)
  Returns an array of possible substitutions for the specified string.
- [- guessesForWord:](./nsspellchecker/guessesforword_.md)
  Returns an array of suggested spellings for the misspelled word.
### Managing the Spell-Checking Process
- [class func uniqueSpellDocumentTag() -> Int](./nsspellchecker/uniquespelldocumenttag%28%29.md)
  Returns a guaranteed unique tag to use as the spell-document tag for a document.
- [func closeSpellDocument(withTag: Int)](./nsspellchecker/closespelldocument%28withtag%29.md)
  Notifies the receiver that the user has finished with the tagged document.
- [func ignoreWord(String, inSpellDocumentWithTag: Int)](./nsspellchecker/ignoreword%28_,inspelldocumentwithtag%29.md)
  Instructs the spell checker to ignore all future occurrences of `wordToIgnore` in the document identified by `tag`.
- [func ignoredWords(inSpellDocumentWithTag: Int) -> [String]?](./nsspellchecker/ignoredwords%28inspelldocumentwithtag%29.md)
  Returns the array of ignored words for a document identified by `tag`.
- [func setIgnoredWords([String], inSpellDocumentWithTag: Int)](./nsspellchecker/setignoredwords%28_,inspelldocumentwithtag%29.md)
  Initializes the ignored-words document (a dictionary identified by `tag` with `someWords`), an array of words to ignore.
- [func setWordFieldStringValue(String)](./nsspellchecker/setwordfieldstringvalue%28_%29.md)
  Sets the string that appears in the misspelled word field, using the string object `aString`.
- [func updateSpellingPanel(withMisspelledWord: String)](./nsspellchecker/updatespellingpanel%28withmisspelledword%29.md)
  Causes the spell checker to update the Spelling panel’s misspelled-word field to reflect `word`.
- [func completions(forPartialWordRange: NSRange, in: String, language: String?, inSpellDocumentWithTag: Int) -> [String]?](./nsspellchecker/completions%28forpartialwordrange,in,language,inspelldocumentwithtag%29.md)
  Provides a list of complete words that the user might be trying to type based on a partial word in a given string.
- [func hasLearnedWord(String) -> Bool](./nsspellchecker/haslearnedword%28_%29.md)
  Indicates whether the spell checker has learned a given word.
- [func unlearnWord(String)](./nsspellchecker/unlearnword%28_%29.md)
  Tells the spell checker to unlearn a given word.
- [func learnWord(String)](./nsspellchecker/learnword%28_%29.md)
  Adds the word to the spell checker dictionary.
- [func userQuotesArray(forLanguage: String) -> [String]](./nsspellchecker/userquotesarray%28forlanguage%29.md)
  Returns the default values for quote replacement.
- [var userReplacementsDictionary: [String : String]](./nsspellchecker/userreplacementsdictionary.md)
  Returns the dictionary used when replacing words.
- [- forgetWord:](./nsspellchecker/forgetword_.md)
  Remove this word from the spelling dictionary.
### Data Detector Interaction
- [func menu(for: NSTextCheckingResult, string: String, options: [NSSpellChecker.OptionKey : Any]?, atLocation: NSPoint, in: NSView) -> NSMenu?](./nsspellchecker/menu%28for,string,options,atlocation,in%29.md)
  Provides a menu containing contextual menu items suitable for certain kinds of detected results.
- [NSSpellChecker.OptionKey](./nsspellchecker/optionkey.md)
  Constants that define options for text checking.
### Automatic Spelling Correction
- [func correction(forWordRange: NSRange, in: String, language: String, inSpellDocumentWithTag: Int) -> String?](./nsspellchecker/correction%28forwordrange,in,language,inspelldocumentwithtag%29.md)
  Returns a single proposed correction if a word is mis-spelled.
- [func showCorrectionIndicator(of: NSSpellChecker.CorrectionIndicatorType, primaryString: String, alternativeStrings: [String], forStringIn: NSRect, view: NSView, completionHandler: ((String?) -> Void)?)](./nsspellchecker/showcorrectionindicator%28of,primarystring,alternativestrings,forstringin,view,completionhandler%29.md)
  Display a suitable user interface to indicate a correction may need to be made.
- [func record(NSSpellChecker.CorrectionResponse, toCorrection: String, forWord: String, language: String?, inSpellDocumentWithTag: Int)](./nsspellchecker/record%28_,tocorrection,forword,language,inspelldocumentwithtag%29.md)
  Records the user response to the correction indicator being displayed.
- [func dismissCorrectionIndicator(for: NSView)](./nsspellchecker/dismisscorrectionindicator%28for%29.md)
  Dismisses the correction indicator for the specified view.
- [NSSpellChecker.CorrectionIndicatorType](./nsspellchecker/correctionindicatortype.md)
  Constants that allow an app to specify the correction indicator type displayed.
- [NSSpellChecker.CorrectionResponse](./nsspellchecker/correctionresponse.md)
  The correction response passed to the[`record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)`](./nsspellchecker/record%28_,tocorrection,forword,language,inspelldocumentwithtag%29.md) method.
### Notifications
- [class let didChangeAutomaticSpellingCorrectionNotification: NSNotification.Name](./nsspellchecker/didchangeautomaticspellingcorrectionnotification.md)
  This notification is posted when the spell checker did change text using automatic spell checking correction. The are posted to the application’s default notification center.
- [class let didChangeAutomaticTextReplacementNotification: NSNotification.Name](./nsspellchecker/didchangeautomatictextreplacementnotification.md)
  Posted when the spell checker changed text using automatic text replacement.  This notification is posted to the app’s default notification center.
- [NSSpellCheckerDidChangeAutomaticInlinePredictionNotification](./nsspellcheckerdidchangeautomaticinlinepredictionnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticInlinePredictionMessage`](./nsspellchecker/didchangeautomaticinlinepredictionmessage.md).
### Type Properties
- [class let didChangeAutomaticCapitalizationNotification: NSNotification.Name](./nsspellchecker/didchangeautomaticcapitalizationnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticCapitalizationMessage`](./nsspellchecker/didchangeautomaticcapitalizationmessage.md).
- [class let didChangeAutomaticDashSubstitutionNotification: NSNotification.Name](./nsspellchecker/didchangeautomaticdashsubstitutionnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticDashSubstitutionMessage`](./nsspellchecker/didchangeautomaticdashsubstitutionmessage.md).
- [class let didChangeAutomaticPeriodSubstitutionNotification: NSNotification.Name](./nsspellchecker/didchangeautomaticperiodsubstitutionnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticPeriodSubstitutionMessage`](./nsspellchecker/didchangeautomaticperiodsubstitutionmessage.md).
- [class let didChangeAutomaticQuoteSubstitutionNotification: NSNotification.Name](./nsspellchecker/didchangeautomaticquotesubstitutionnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticQuoteSubstitutionMessage`](./nsspellchecker/didchangeautomaticquotesubstitutionmessage.md).
- [class let didChangeAutomaticTextCompletionNotification: NSNotification.Name](./nsspellchecker/didchangeautomatictextcompletionnotification.md)
  To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticTextCompletionMessage`](./nsspellchecker/didchangeautomatictextcompletionmessage.md).
- [class var isAutomaticCapitalizationEnabled: Bool](./nsspellchecker/isautomaticcapitalizationenabled.md)
- [class var isAutomaticDashSubstitutionEnabled: Bool](./nsspellchecker/isautomaticdashsubstitutionenabled.md)
- [class var isAutomaticInlinePredictionEnabled: Bool](./nsspellchecker/isautomaticinlinepredictionenabled.md)
- [class var isAutomaticPeriodSubstitutionEnabled: Bool](./nsspellchecker/isautomaticperiodsubstitutionenabled.md)
- [class var isAutomaticQuoteSubstitutionEnabled: Bool](./nsspellchecker/isautomaticquotesubstitutionenabled.md)
- [class var isAutomaticSpellingCorrectionEnabled: Bool](./nsspellchecker/isautomaticspellingcorrectionenabled.md)
- [class var isAutomaticTextCompletionEnabled: Bool](./nsspellchecker/isautomatictextcompletionenabled.md)
- [class var isAutomaticTextReplacementEnabled: Bool](./nsspellchecker/isautomatictextreplacementenabled.md)
### Instance Methods
- [func deletesAutospaceBetweenString(String, andString: String, language: String?) -> Bool](./nsspellchecker/deletesautospacebetweenstring%28_,andstring,language%29.md)
- [func language(forWordRange: NSRange, in: String, orthography: NSOrthography?) -> String?](./nsspellchecker/language%28forwordrange,in,orthography%29.md)
- [func preventsAutocorrection(before: String, language: String?) -> Bool](./nsspellchecker/preventsautocorrection%28before,language%29.md)
- [func requestCandidates(forSelectedRange: NSRange, in: String, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult]) -> Void)?) -> Int](./nsspellchecker/requestcandidates%28forselectedrange,in,types,options,inspelldocumentwithtag,completionhandler%29.md)
- [func showInlinePrediction(forCandidates: [NSTextCheckingResult], client: any NSTextInputClient)](./nsspellchecker/showinlineprediction%28forcandidates,client%29.md)
- [func ignoreGrammarRange(NSRange, inSentence: String, inSpellDocumentWithTag: Int)](./nsspellchecker/ignoregrammarrange%28_,insentence,inspelldocumentwithtag%29.md)
### Structures
- [NSSpellChecker.DidChangeAutomaticCapitalizationMessage](./nsspellchecker/didchangeautomaticcapitalizationmessage.md)
- [NSSpellChecker.DidChangeAutomaticDashSubstitutionMessage](./nsspellchecker/didchangeautomaticdashsubstitutionmessage.md)
- [NSSpellChecker.DidChangeAutomaticInlinePredictionMessage](./nsspellchecker/didchangeautomaticinlinepredictionmessage.md)
- [NSSpellChecker.DidChangeAutomaticPeriodSubstitutionMessage](./nsspellchecker/didchangeautomaticperiodsubstitutionmessage.md)
- [NSSpellChecker.DidChangeAutomaticQuoteSubstitutionMessage](./nsspellchecker/didchangeautomaticquotesubstitutionmessage.md)
- [NSSpellChecker.DidChangeAutomaticSpellingCorrectionMessage](./nsspellchecker/didchangeautomaticspellingcorrectionmessage.md)
- [NSSpellChecker.DidChangeAutomaticTextCompletionMessage](./nsspellchecker/didchangeautomatictextcompletionmessage.md)
- [NSSpellChecker.DidChangeAutomaticTextReplacementMessage](./nsspellchecker/didchangeautomatictextreplacementmessage.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Spell-checking
- [protocol NSChangeSpelling](./nschangespelling.md)
  A protocol that responder objects can implement to correct a misspelled word.
- [protocol NSIgnoreMisspelledWords](./nsignoremisspelledwords.md)
  A protocol that enables the Ignore button in the Spelling panel to function properly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker)*